from datetime import datetime
from functools import cache
import json
import logging
import re
from typing import Optional
from bs4 import BeautifulSoup
import pandas as pd
import os
import xml.etree.cElementTree as ET

import requests

def _load_databases():
    """Load databases configuration from JSON file."""
    databases_path = os.path.join(os.path.dirname(__file__), 'databases.json')
    with open(databases_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load databases configuration
DATABASES = _load_databases()

class BlsRepository:
    _root_dir: str
    _bls_dirname: str # where BLS data is stored
    _products_dirname: str # where repackaged data products are stored
    _databases: dict[str,"BlsDatabase"]

    def __init__(self, root, bls_dirname='bls', products_dirname='products'):
        self._root_dir = root
        self._bls_dirname = bls_dirname
        self._products_dirname = products_dirname
        self._databases = None

    @property
    def root_dir(self):
        return self._root_dir

    @property 
    def bls_dir(self):
        dirpath = os.path.join(self.root_dir, self._bls_dirname)
        os.makedirs(dirpath, exist_ok=True)
        return dirpath

    @property
    def databases(self):
        if self._databases is None:
            for id in DATABASES:
                self._databases[id] = BlsDatabase(self, id)
        return self._databases

    @property 
    def database_ids(self, supported=True):
        """Get the list of database identifiers.
        """
        return list(self.databases.keys())

    @property
    def products_dir(self):
        dirpath = os.path.join(self.root_dir, self._products_dirname)
        os.makedirs(dirpath, exist_ok=True)
        return dirpath
    
class BlsDatabase:
    _repository: BlsRepository
    _id: str
    _files: dict[str,"BlsFile"]|None
    _bls_files: dict[str,dict]|None

    BLS_REQUEST_HEADERS = {
    	"Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
	    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    def __init__(self, repository, id):
        self._repository = repository
        self._id = id
        self._files = None
        self._bls_files = None
        if id not in DATABASES:
            raise ValueError(f"Unknown database id: {id}")

    @property 
    def bls_dir(self):
        dirpath = os.path.join(self.repository.bls_dir, self._id)
        os.makedirs(dirpath, exist_ok=True)
        return dirpath

    @property
    def bls_url(self):
        return f"https://download.bls.gov/pub/time.series/{self.id}"

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return DATABASES[self.id].get('name')

    @property
    def repository(self):
        return self._repository

    @property
    def files(self):
        if not self._files:
            self._files = {}
            for filename in os.listdir(self.bls_dir):
                if not filename.startswith(f"{self.id}."): # only <id>.* files
                    continue
                extension = filename.split('.')[-1]
                if filename.startswith(f"{self.id}.data."):
                    self._files[filename] = BlsDataFile(self, filename)
                elif extension in [
                    'absn','activity','ages','area','area_type','base','born','category','cert','characteristics','chld','class','county',
                    'dataclass','dataelement','datatype','demographics','disa','display','duration',
                    'education','eductrn','entr','estimate','expr','footnote','hheader','hour',
                    'index','industry','indy','item','jdes','measure','lfst','look','mari','mjhs','msa','occupation',
                    'orig','otjt','owner','ownership','pcts','period','periodicity','process',
                    'race','rank','ratelevel','rjnw','rnlf','rwns','seasonal','seek','sector','sexs','sizeclass','state','srd',
                    'subcategory','subcell','supersector','tdat','tlwk','type','unitanalysis','vets','wkex','wkst'
                    ]:
                    self._files[filename] = BlsCodeFile(self, filename)
                elif extension == 'contacts':
                    self._files[filename] = BlsContactsFile(self, filename)
                elif extension == 'series':
                    self._files[filename] = BlsSeriesFile(self, filename)
                elif extension == 'txt':
                    self._files[filename] = BlsTxtFile(self, filename)
                else:
                    self._files[filename] = BlsFile(self, filename)
        return self._files
    

    @property
    def files_updated_range(self) -> tuple[datetime, datetime]|None:
        """Get the range of file update timestamps for the local repository."""
        if not self.files:
            return None
        return min(file.updated for file in self.files.values()), max(file.updated for file in self.files.values())

    @property
    def files_bls_updated_range(self) -> tuple[datetime, datetime]|None:
        """Get the range of file update timestamps for BLS repository."""
        bls_files = self.scrape_database_files().values()
        if bls_files:
            return (min(file.get("date") for file in bls_files), max(file.get("date") for file in bls_files))

    @property
    def codefiles(self) -> dict[str, "BlsCodeFile"] :
        """The list of code files in this dataset"""
        files = {}
        for filename,file in self.files.items():
            if isinstance(file, BlsCodeFile):
                files[filename] = file
        return files

    @property
    def contactsfile(self) -> "BlsContactsFile":
        """The contacts file"""
        for filename, file in self.files.items():
            if isinstance(file, BlsContactsFile):
                return file

    @property
    def datafiles(self) -> dict[str, "BlsDataFile"] :
        """The collection of data files in this dataset"""
        files = {}
        for filename,file in self.files.items():
            if isinstance(file, BlsDataFile):
                files[filename] = file
        return files
    
    @property
    def datafile0(self) -> "BlsDataFile":
        """The 'current' data file"""
        for filename, file in self.datafiles.items():
            if filename.startswith(f"{self.id}.data.0."):
                return file
            
    @property
    def datafile1(self) -> "BlsDataFile":
        """The 'all items' or 'all data' data file"""
        for filename, file in self.datafiles.items():
            if filename.startswith(f"{self.id}.data.1."):
                return file

    @property
    def ddic_filepath(self):
        return os.path.join(self.products_dir, f"{self.id}.ddi25.xml")

    @property
    def series_id_pattern(self):
        """The series_id regular expression pattern for this database"""
        return DATABASES[self.id].get('series_id_pattern')

    @property
    def seriesfile(self) -> "BlsSeriesFile":
        """The <database_id>.series file"""
        for filename, file in self.files.items():
            if isinstance(file, BlsSeriesFile):
                return file

    @property
    def txtfile(self) -> "BlsTxtFile":
        """The <database_id>.txt file"""
        for filename, file in self.files.items():
            if isinstance(file, BlsTxtFile):
                return file

    @property
    def products_dir(self):
        """The directory where the data products are stored"""
        dirpath = os.path.join(self.repository.products_dir, self._id)
        os.makedirs(dirpath, exist_ok=True)
        return dirpath

    @property
    def size(self):
        """The size of the database in bytes"""
        return sum(file.size for file in self.files.values())
    
    @property
    def size_formatted(self):
        return BlsFile.format_size(self.size)

    def get_codelist(self, variable) -> pd.DataFrame|None:
        """Return the codelist for the given variable.
        Matches the variable name on the code file extension.
        """
        # computed code list (not in file)
        if variable == "period_type":
            return  pd.DataFrame({'value': ['M','S'], 'label': ['Month','Semester']})
        # code files
        if self.get_codefile(variable):
            return self.get_codefile(variable).codelist
        return None

    def get_codefile(self, variable) -> Optional["BlsCodeFile"]:
        """Return the code file for the given variable.
        Matches the variable name on the code file extension.
        """
        # code files
        if variable.endswith("_code"): # strip the _code suffix
            variable = variable[:-5]
        elif variable.endswith("_codes"): # strip the _codes suffix
            variable = variable[:-6]
        for file in self.codefiles.values():
            if variable == file.extension:
                return file
        return None

    def get_data_elements(self):
        """Returns a dictionary with the data elements as keys.

        This parses section 7 of the txt file and return the names and label of the data elements.
        - The first four lines are skipped as they are not relevant.
        - Each data element is separated by an empty line that can contain tabs and spaces.
        - the element name is at the beginning of the line. Can be spread across multiple lines.
        - the element label is at the end of the line. Can be spread across multiple lines.
        - empty lines may be present at the end of the section.

        Additional entries are create for known undocumented or derived variables.
        """
        data_elements = {
            "database_id": {"label":"Database identifier"},
            "footnote_codes": {"label":"Series footnotes"},
            "period_type": {"label":"Period type"},
            "period_number": {"label":"Period number"},
            "seasonal_code": {"label":"Seasonal adjustment indicator"},
            "series_id": {"label":"Series identifier"}
        }
        # parse section 7
        lines = iter(self.txtfile.sections[7].splitlines())
        # skip the first 4 lines
        next(lines)
        next(lines)
        next(lines)
        next(lines)
        de_name = ""
        de_label =""
        while True:
            try: 
                line = next(lines)
                if line.strip(" \t\n") == "": # empty line
                    # save data element
                    if de_name:
                        data_elements[de_name] = {"label": de_label.rstrip(".")}
                    de_name = ""
                    de_label = ""
                    continue
                split = line.split("\t")
                # name
                de_name += split[0].strip() # the element name is at the beginning of the line. Can be spread across multiple lines.
                # label
                if de_label.endswith("."): # we have the complete label. Extra lines may come from examples.
                    continue
                if de_label:
                    de_label += " " # add a space if there is already a label
                de_label += split[-1].strip() # the element label is at the end of the line. Can be spread across multiple lines.
            except StopIteration:
                break
        return data_elements

    def get_ddic(self, refresh=False, docDscr=True, stydDscr=True, fileDscr=True, dataDscr=True, file_id=None) -> ET.Element:
        """Generates a DDI-Codebook for the entire database.
        """
        if os.path.isfile(self.ddic_filepath) and not refresh:
            logging.debug(f"Loading database DDI from {self.ddic_filepath}")
            tree = ET.parse(self.ddic_filepath)
            ddi_codebook = tree.getroot()
        else:
            logging.debug("Generating database DDI")
            ddi_codebook = ET.Element("{ddi:codebook:2_5}codeBook")
            ddi_codebook.set("ID", f"us_bls_{self.id}")
            ddi_codebook.set("codeBookAgency", "gov.bls")
            # generate docDscr
            if docDscr:
                ddi_docDscr = ET.SubElement(ddi_codebook, "{ddi:codebook:2_5}docDscr")
                ddi_docDscr_citation = ET.SubElement(ddi_docDscr, "{ddi:codebook:2_5}citation")
                ddi_docDscr_prodStmt = ET.SubElement(ddi_docDscr_citation, "{ddi:codebook:2_5}prodStmt")
                ddi_docDscr_prodStmt_producer = ET.SubElement(ddi_docDscr_prodStmt, "{ddi:codebook:2_5}producer")
                ddi_docDscr_prodStmt_producer.set("abbr","highvaluedata.net")
                ddi_docDscr_prodStmt_producer.text = "High-Value Data Network / Data Artifex"
                ddi_docDscr_prodStmt_prodDate = ET.SubElement(ddi_docDscr_prodStmt, "{ddi:codebook:2_5}prodDate")
                isonow = datetime.now().isoformat()
                ddi_docDscr_prodStmt_prodDate.set("date",isonow)
                ddi_docDscr_prodStmt_prodDate.text = isonow
                ddi_docDscr_prodStmt_software = ET.SubElement(ddi_docDscr_prodStmt, "{ddi:codebook:2_5}software")
                ddi_docDscr_prodStmt_software.text = "usbls-project"
            # generate stdyDscr
            if stydDscr:
                ddi_stdyDscr = ET.SubElement(ddi_codebook, "{ddi:codebook:2_5}stdyDscr")
                ddi_stdyDscr_citation = ET.SubElement(ddi_stdyDscr, "{ddi:codebook:2_5}citation")
                ddi_stdyDscr_citation_titlStmt = ET.SubElement(ddi_stdyDscr_citation, "{ddi:codebook:2_5}titlStmt")
                ddi_stdyDscr_citation_titlStmt_titl = ET.SubElement(ddi_stdyDscr_citation_titlStmt, "{ddi:codebook:2_5}titl")
                ddi_stdyDscr_citation_titlStmt_titl.text = DATABASES[self.id]['name']
                ddi_stdyDscr_citation_rspStmt = ET.SubElement(ddi_stdyDscr_citation, "{ddi:codebook:2_5}rspStmt")
                ddi_stdyDscr_citation_rspStmtAuthEnty = ET.SubElement(ddi_stdyDscr_citation_rspStmt, "{ddi:codebook:2_5}AuthEnty")
                ddi_stdyDscr_citation_rspStmtAuthEnty.text = "United States Bureau of Labour Statistics"
                # generate stdyInfo
                ddi_stdyDscr_stdyInfo = ET.SubElement(ddi_stdyDscr, "{ddi:codebook:2_5}stdyInfo")
                ddi_stdyDscr_stdyInfo_abstract = ET.SubElement(ddi_stdyDscr_stdyInfo, "{ddi:codebook:2_5}abstract")
                ddi_stdyDscr_stdyInfo_abstract.text = self.txtfile.description
                ddi_stdyDscr_stdyInfo_abstract.set("xml:space","preserve")
            if fileDscr:
                # find smallest data file to get variables
                reference_datafile = None
                for file in self.datafiles.values():
                    if reference_datafile is None or file.size < reference_datafile.size:
                        reference_datafile = file
                reference_df = reference_datafile.get_pandas_df()
                # generate fileDscr
                datafile_ids = []
                for filename,datafile in self.datafiles.items():
                    datafile_id = f"F{datafile.number}"
                    if file_id and datafile_id not in file_id: # file id filter
                        continue
                    datafile_ids.append(datafile_id)
                    ddi_fileDscr = ET.SubElement(ddi_codebook, "{ddi:codebook:2_5}fileDscr")
                    ddi_fileDscr.set("ID",datafile_id)
                    ddi_fileTxt = ET.SubElement(ddi_fileDscr, "{ddi:codebook:2_5}fileTxt")
                    ddi_fileName = ET.SubElement(ddi_fileTxt, "{ddi:codebook:2_5}fileName")
                    ddi_fileName.text = filename
            # generate dataDscr
            if dataDscr:
                ddi_dataDsrc = ET.SubElement(ddi_codebook, "{ddi:codebook:2_5}dataDscr")
                data_elements = self.get_data_elements()
                for name,series in reference_df.items():
                    ddi_var = ET.SubElement(ddi_dataDsrc,"{ddi:codebook:2_5}var")
                    # attributes
                    ddi_var.set("ID", name)
                    ddi_var.set("name", name)
                    ddi_var.set("files", ",".join(datafile_ids))
                    ddi_var_labl = ET.SubElement(ddi_var, "{ddi:codebook:2_5}labl")
                    # label
                    label = None
                    data_element = data_elements.get(name)
                    if data_element:
                        label = data_element['label']
                    ddi_var_labl.text = label if label else name
                    # format
                    dtype = series.dtype.name
                    ddi_var_format = ET.SubElement(ddi_var, "{ddi:codebook:2_5}varFormat")
                    if dtype in ["int64","float64"]:
                        ddi_var_format.set("type","numeric")
                        if dtype.startswith("int"):
                            ddi_var.set("dcml","0")
                        else:
                            ddi_var.set("dcml","3")
                        ddi_var_format.set("formatname", series.dtype.name)
                    else:
                        ddi_var_format.set("type","character")
                        ddi_var_format.set("formatname", "string")

                    # add codelist
                    codelist_df = self.get_codelist(name)
                    if codelist_df is not None:
                        for index, row in codelist_df.iterrows(): 
                            ddi_catgry = ET.SubElement(ddi_var, "{ddi:codebook:2_5}catgry")
                            ddi_catValu = ET.SubElement(ddi_catgry, "{ddi:codebook:2_5}catValu")
                            ddi_catValu.text = row.iloc[0]
                            ddi_labl = ET.SubElement(ddi_catgry, "{ddi:codebook:2_5}labl")
                            ddi_labl.text = row.iloc[1]                    
        return ddi_codebook

    def get_series_attributes(self):
        """
        Parses the variable in the .series files and returns variables that are not part of the series_id.

        Returns a list of classifier names.
        """
        attributes = []
        if not self.seriesfile:
            return attributes
            
        series_df = self.seriesfile.get_pandas_df()
        if series_df is None or series_df.empty:
            return attributes

        # Get all column names from the series file
        all_columns = set(series_df.columns)

        # Extract component names from the series_id_pattern
        series_components_names = set()
        for component in self.get_series_components():
            series_components_names.add(component['name'])

        # Standard columns that are not classifiers

        # Find attribute columns: columns that are not standard and not part of series_id
        attribute_columns = all_columns - series_components_names

        for attribute_name in sorted(attribute_columns):
            if attribute_name == 'series_id': # skip series_id itself
                continue
            attribute = {'name': attribute_name}
            if attribute_name.startswith('seasonal'):
                attribute['type'] = 'time'
            elif attribute_name.endswith('_code') or attribute_name.endswith('_codes'):
                attribute['type'] = 'code'
            elif attribute_name.endswith('_year') or attribute_name.endswith('_period') or attribute_name.startswith('seasonal'):
                attribute['type'] = 'time'
            elif attribute_name.endswith('_name') or attribute_name.endswith('_text') or attribute_name.endswith('_title') or attribute_name.endswith('_desc'):
                attribute['type'] = 'text'
            else:
                attribute['type'] = 'other'
            attributes.append(attribute)

        return attributes

    def get_series_components(self):
        """
        Parses the series_id_pattern and returns a list of components.

        Returns a list of dictionaries with the following keys:
          - name: The name of the component
          - class: The class of the component
          - length: The length of the component
          - pattern: The regex pattern for the component
        """
        # get series components from series_id_pattern
        pattern = self.series_id_pattern
        components = []
        if pattern:
            named_groups = re.findall(r'\?P<(\w+)>\[([^\]]+)\](?:\{(\d+(?:-\d+)?)\}|(\*))', pattern)
            for name, char_class, length1, length2 in named_groups:
                length = length1 if length1 else length2
                if length == '*':
                    length_val = '*'
                    length_pattern = '*'
                elif '-' in length:
                    length_val = length  # keep the range as-is (e.g., "1-5")
                    length_pattern = f'{{{length}}}'
                else:
                    length_val = int(length)  # single number
                    length_pattern = f'{{{length}}}'
                components.append({
                    'name': name,
                    'class': char_class,
                    'length': length_val,
                    'pattern': f'?P<{name}>[{char_class}]{length_pattern}'
                })
        return components

    def to_ddic(self):
        """Saves DDI-Codebook for the entire database."""
        ET.register_namespace('', 'ddi:codebook:2_5')
        tree = ET.ElementTree(self.get_ddic(refresh=True))
        tree.write(self.ddic_filepath, encoding="utf-8", xml_declaration=True)

    def harvest(self, overwrite=False):
        """Harvest files from the BLS website.
        """
        if not os.path.isdir(self.bls_dir):
            os.mkdir(self.bls_dir)
        files = self.scrape_database_files().values()
        if files:
            for file in files:
                bls_file = BlsFile(self, file['name'])
                # check if we already have this file
                if bls_file.exists and not overwrite:
                    if bls_file.updated >= file['date'] and bls_file.size == file['size']:
                        logging.info(f"Skipping {file['name']} (up to date)")
                        continue
                # download 
                bls_file.download()

    def scrape_database_files(self) -> dict[str,dict]:
        """Scrape file information from BLS HTML page
        """
        if self._bls_files is None:
            logging.info(f"Scraping {self.id}")
            response = requests.get(self.bls_url, headers=BlsDatabase.BLS_REQUEST_HEADERS)
            self._bls_files = {}
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                rex = re.compile(r'^\s*(\d{1,2}\/\d{1,2}\/\d{4})\s*(\d{1,2}:\d{1,2}\s.{2})\s*(\d*).*$')
                for a in soup.find_all('a'):
                    if a.string.startswith('[To Parent'):
                        continue
                    file_info = {'name': a.string}
                    a.nextSibling # <br/>
                    info = str(a.previousSibling)
                    if '<dir>' in info:
                        continue
                    m = rex.match(info)
                    if m:
                        file_info['date'] = datetime.strptime(f"{m.group(1)} {m.group(2)}",'%m/%d/%Y %I:%M %p')
                        file_info['size'] = int(m.group(3))
                    self._bls_files[a.string] = file_info
            else:
                logging.error(f"Error {response.status_code} scraping {self.id}")
        return self._bls_files

class BlsFile:
    _database: BlsDatabase
    _filename: str
    _extension: str
    _size: int
    _updated: str

    def __init__(self, database, filename):
        self._database = database
        self._filename = filename
        self._extension = filename.split('.')[-1]
        self.refresh_stats()

    @property
    def bls_url(self) -> str:
        return f"{self.database.bls_url}/{self.filename}"
    
    @property
    def database(self) -> BlsDatabase:
        return self._database
    
    @property
    def extension(self) -> str:
        return self._extension
    
    @property
    def exists(self) -> bool:
        return os.path.isfile(self.filepath)
    
    @property
    def filename(self) -> str:
        return self._filename
    
    @property
    def filepath(self) -> str:
        return os.path.join(self.database.bls_dir, self._filename)

    @property
    def name(self) -> str:
        return self._filename

    @property
    def number(self) -> int:
        tokens = self.filename.split(".")
        return int(tokens[2])

    @property
    def size(self) -> int:
        return self._size
    
    @property
    def size_formatted(self) -> str:
        if self.size:
            return BlsFile.format_size(self._size)

    @property
    def series_id_pattern(self):
        return self.database.series_id_pattern

    @property
    def suffix(self) -> str:
        tokens = self.filename.split(".")
        return str(tokens[3])

    @property
    def updated(self) -> datetime:
        return self._updated
    

    @property
    def csv_filepath(self) -> str:
        if isinstance(self, BlsCodeFile):
            extension = '.codes.csv'
        else:
            extension = '.csv'
        filepath = os.path.join(self.database.products_dir, self.filename + extension)
        return filepath

    @property
    def parquet_filepath(self) -> str:
        if isinstance(self, BlsCodeFile):
            extension = '.codes.parquet'
        else:
            extension = '.parquet'
        filepath = os.path.join(self.database.products_dir, self.filename + extension)
        return filepath
        
    @staticmethod
    def format_size(size) -> str:
        """Formats a file size in bytes as KB or MB.
        """
        KB = 1024
        MB = KB ** 2
        if size < MB:
            return f"{size / KB:.2f} KB"
        else:
            return f"{size / MB:.2f} MB"
        
    def download(self, chunk_size=1024*1024, max_retries=3, timeout=30) -> None:
        """ Downloads the file from the BLS website with robust error handling.
        
        Args:
            chunk_size: Size of chunks to download (default: 1MB)
            max_retries: Maximum number of retry attempts (default: 3)
            timeout: Request timeout in seconds (default: 30)
        """
        import time
        from requests.exceptions import RequestException, Timeout, ConnectionError
        
        temp_filepath = f"{self.filepath}.tmp"
        
        for attempt in range(max_retries):
            try:
                logging.info(f"Downloading {self.bls_url} (attempt {attempt + 1}/{max_retries})")
                
                # Download with streaming (don't rely on HEAD for size - can be compressed/different)
                with requests.get(
                    self.bls_url, 
                    headers=BlsDatabase.BLS_REQUEST_HEADERS, 
                    stream=True,
                    timeout=timeout
                ) as r:
                    r.raise_for_status()
                    
                    # Try to get expected size from response headers
                    total_size = int(r.headers.get('content-length', 0))
                    if total_size > 0:
                        logging.info(f"Expected size: {self.format_size(total_size)}")
                    
                    downloaded = 0
                    last_log_time = time.time()
                    log_interval = 5  # Log progress every 5 seconds
                    
                    with open(temp_filepath, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=chunk_size):
                            if chunk:  # filter out keep-alive new chunks
                                f.write(chunk)
                                downloaded += len(chunk)
                                
                                # Log progress periodically
                                current_time = time.time()
                                if total_size > 0 and (current_time - last_log_time) >= log_interval:
                                    progress_pct = (downloaded / total_size) * 100
                                    downloaded_fmt = self.format_size(downloaded)
                                    total_fmt = self.format_size(total_size)
                                    logging.info(f"Progress: {progress_pct:.1f}% ({downloaded_fmt} / {total_fmt})")
                                    last_log_time = current_time
                
                # Check if file was actually downloaded
                if not os.path.exists(temp_filepath):
                    raise IOError("Downloaded file does not exist")
                
                actual_size = os.path.getsize(temp_filepath)
                if actual_size == 0:
                    raise IOError("Downloaded file is empty")
                
                # Log size info but don't fail on mismatch
                # (Content-Length can be wrong due to compression, line endings, etc.)
                if total_size > 0:
                    size_diff = abs(actual_size - total_size)
                    if size_diff > 0:
                        size_diff_pct = (size_diff / total_size) * 100
                        logging.debug(f"Downloaded size: {self.format_size(actual_size)} vs expected: {self.format_size(total_size)} (diff: {size_diff_pct:.1f}%)")
                
                # Move temp file to final location
                if os.path.exists(self.filepath):
                    os.remove(self.filepath)
                os.rename(temp_filepath, self.filepath)
                
                logging.info(f"Download completed: {self.filepath} ({self.format_size(actual_size)})")
                self.refresh_stats()
                return
                
            except (RequestException, Timeout, ConnectionError, IOError) as e:
                logging.warning(f"Download attempt {attempt + 1} failed: {str(e)}")
                
                # Clean up temp file if it exists
                if os.path.exists(temp_filepath):
                    try:
                        os.remove(temp_filepath)
                    except:
                        pass
                
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                    logging.info(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    logging.error(f"Failed to download {self.bls_url} after {max_retries} attempts")
                    raise
    
    def refresh_stats(self) -> None:
        """Refreshes the file statistics.
        """
        if os.path.isfile(self.filepath):
            stats = os.lstat(self.filepath)
            self._size = stats.st_size
            self._updated = datetime.fromtimestamp(stats.st_mtime)
        else:
            self._size = None
            self._updated = None
    

    def to_csv(self, overwrite=False, zipped=False):
        """Saves the file in CSV format.
        Only available for files that have a dataframe.        
        """
        if hasattr(self,'_pandas_df'):
            filepath = f"{self.csv_filepath}.zip" if zipped else self.csv_filepath
            if os.path.isfile(filepath):
                # file already exists
                stats = os.lstat(filepath)
                updated = datetime.fromtimestamp(stats.st_mtime)
                if updated < self.updated:
                    # file is outdated
                    logging.info(f"Updating {filepath}")
                elif not overwrite:
                    # file is up to date
                    logging.info(f"Skipping {filepath} (already exists)")
                    return
            logging.info(f"Saving {filepath}")
            self.get_pandas_df().to_csv(filepath, index=False) # will automatically compress is extension is .zip
        else:
            logging.warning("File does not have a dataframe.")

    def to_parquet(self, overwrite=False):
        """Saves the file in parquet format.

        Only available for files that have a dataframe.
        """
        if hasattr(self,'_pandas_df'):
            if os.path.isfile(self.parquet_filepath):
                # file already exists
                stats = os.lstat(self.filepath)
                csv_updated = datetime.fromtimestamp(stats.st_mtime)
                if csv_updated < self.updated:
                    # file is outdated
                    logging.info(f"Updating {self.parquet_filepath}")
                elif not overwrite:
                    # file is up to date
                    logging.info(f"Skipping {self.parquet_filepath} (already exists)")
                    return
            logging.info(f"Saving {self.parquet_filepath}")
            self.get_pandas_df().to_parquet(self.parquet_filepath, index=False)
        else:
            logging.warning("File does not have a dataframe.")

class BlsCodeFile(BlsFile):    
    _pandas_df = None

    def __init__(self, database, name):
        super().__init__(database, name)

    @property
    def codelist(self) -> pd.DataFrame|None:
        """
        Returns a 2-column Pandas DataFrame with the code list value and label.
        """
        value_col_names = [self.extension+'_code', self.extension]
        value_col_name = [x for x in value_col_names if x in self.get_pandas_df().columns] # this returns an array
        value_col_name = value_col_name[0] if value_col_name else None
        label_col_names = [self.extension+'_name', self.extension+'_text', self.extension+'_title', self.extension+'_desc']
        label_col_name = [x for x in label_col_names if x in self.get_pandas_df().columns] # this returns an array
        label_col_name = label_col_name[0] if label_col_name else None
        if not value_col_name:
            logging.error(f"Code value column {value_col_name} not found in {self.filename}")
        if not label_col_name:
            logging.warning(f"Code label column {label_col_name} not found in {self.filename}")
        if value_col_name and label_col_name:
            codelist_df = self.get_pandas_df()[[value_col_name, label_col_name]]
            return codelist_df

    def get_pandas_df(self):
        if os.path.isfile(self.filepath):
            if self._pandas_df is None:
                logging.debug(f"Loading {self.filepath}")
                self._pandas_df = pd.read_csv(self.filepath, delimiter="\t", low_memory=False)
                # Hard coded fixes for known issues (column names, recodes)
                if self.database.id == 'ce':
                    if self.extension == 'datatype': 
                        logging.debug("Patching ce.datatype code columns")
                        self._pandas_df = self._pandas_df.rename(columns={
                            'data_type_code': 'datatype_code',
                            'data_type_text': 'datatype_text'
                        })
                elif self.database.id == 'ep':
                    if self.extension == 'display':
                        logging.debug("Patching ep.display code columns")
                        self._pandas_df = self._pandas_df.rename(columns={
                            'disp_code': 'display_code',
                            'disp_desc': 'display_desc'
                        })
                    elif self.extension == 'industry':
                        logging.debug("Patching ep.industry code columns")
                        self._pandas_df = self._pandas_df.rename(columns={
                            'ind_code': 'industry_code',
                            'ind_title': 'industry_title'
                        })
                    elif self.extension == 'occupation': 
                        logging.debug("Patching ep.occupation code columns")
                        self._pandas_df = self._pandas_df.rename(columns={
                            'occ_code': 'occupation_code',
                            'occ_title': 'occupation_title'
                        })
                        # TODO: do we want to remove dash character at position three in 'occ_code' column 1?
                        # e.g. 00-0000 --> 000000
                        # logging.debug("Patching ep.occupation codes")
                        # self._pandas_df['occupation_code'] = self._pandas_df['occupation_code'].apply(lambda x: x[:2] + x[3:])

                elif self.database.id == 'la':
                    if self.extension == 'area_type':
                        logging.debug("Patching la.area_type code columns")
                        self._pandas_df = self._pandas_df.rename(columns={
                            'areatype_text': 'area_type_text'
                        })
        else:
            logging.error(f"File not found: {self.filepath}")
        return self._pandas_df


class BlsContactsFile(BlsFile):    
    def __init__(self, database, name):
        super().__init__(database, name)


class BlsDataFile(BlsFile):
    _pandas_df = None
    _spark_df = None
    _stats = None

    def __init__(self, database, filename):
        super().__init__(database, filename)

    @property
    def ddic_filepath(self):
        return os.path.join(self.database.products_dir, f"{self.filename}.ddi25.xml")

    @property
    def topic(self):
        return self.filename.rsplit(".", 1)[1]

    def get_pandas_df(self, refresh=False, from_parquet=False) -> pd.DataFrame | None:
        """Returns the Pandas DataFrame for this data file.
        Loads the CSV data, applies various cleansing steps, and computes derived variables.
        If from_parquet is True, the dataframe is loaded from the parquet file instead.
        """
        if os.path.isfile(self.filepath):
            if self._pandas_df is None or refresh:
                if os.path.isfile(self.parquet_filepath) and from_parquet:
                    logging.debug(f"Loading {self.parquet_filepath}")
                    self._pandas_df = pd.read_parquet(self.parquet_filepath)
                else: # load from BLS data file
                    logging.debug(f"Loading {self.filepath}")
                    # know data types
                    known_dtype={'footnote_codes': 'str'}
                    # load from raw CSV
                    self._pandas_df = pd.read_csv(self.filepath, delimiter="\t", dtype=known_dtype, low_memory=False)
                    # remove spaces from column names
                    self._pandas_df.columns = self._pandas_df.columns.str.strip()
                    # remove spaces from series_id values
                    self._pandas_df['series_id'] = self._pandas_df['series_id'].str.strip()
                    # replace non-numeric values with NaN
                    self._pandas_df['value'] = pd.to_numeric(self._pandas_df['value'], errors='coerce')
                    non_numeric_count = self._pandas_df['value'].isna().sum()
                    if non_numeric_count > 0:
                        logging.warning(f"Non-numeric values in {self.filepath}: {non_numeric_count}")
                    # make sure footnote codes are string
                    if 'footnote_codes' in self._pandas_df.columns:
                        self._pandas_df['footnote_codes'] = self._pandas_df['footnote_codes'].apply(lambda x: str(x) if not pd.isnull(x) else None)
                    # ENRICH DATAFRAME
                    # add year_period column
                    self._pandas_df['year_period'] = self._pandas_df['year'].astype(str)+ '-' + self._pandas_df['period']
                    # add period_type
                    self._pandas_df['period_type'] = self._pandas_df['period'].str[0:1]
                    # add period_number
                    self._pandas_df['period_number'] = self._pandas_df['period'].str[1:].astype(int)
                    # add series_id variables
                    if self.database.series_id_pattern is not None:
                        # This nice one liner uses the SERIES_ID_PATTERN to extract components of the series_id and create new colums as named with ?P<> in the regex
                        # The ** operator unpacks the dictionary created by str.extract (containing extracted data with field names as keys) into new columns
                        self._pandas_df = self._pandas_df.assign(**self._pandas_df['series_id'].str.extract(self.database.series_id_pattern))
                        # if needed, the field names can be extracted with:
                        # field_names = re.findall(r"(?P<(?P<name>\w+>))", pattern)
        else:
            logging.error(f"File not found: {self.filepath}")
        return self._pandas_df

    @property
    def spark_df(self):
        """Returns a Spark DataFrame.
        """
        if os.path.isfile(self.filepath):
            if self._spark_df is None:
                logging.debug(f"Loading {self.filepath}")
                self._spark_df = pd.read_csv(self.filepath, delimiter="\t", low_memory=False)
        return self._spark_df

    @property
    def stats(self):
        if not self._stats:
            self._stats = {}
            df = self.get_pandas_df()
            self._stats['size'] = self.size_formatted
            self._stats['updated'] = self.updated
            self._stats['n_records'] = df.shape[0]
            self._stats['n_series'] = df['series_id'].nunique()
            self._stats['years'] = sorted(df['year'].unique())
            self._stats['periods'] = sorted(df['period'].unique())
            (period_from,period_to) = self.get_time_period()
            self._stats['period_from'] = period_from
            self._stats['period_to'] = period_to
            self._stats['n_missing_values'] = df['value'].isnull().sum()
            #self._stats['footnote_codes'] = sorted(df['footnote_codes'].unique())
            self._stats['n_footnotes'] = df['footnote_codes'].isnull().sum()
        return self._stats

    def get_col_datatype(self, col_name):
        return self.get_pandas_df()[col_name].dtype

    def get_col_codelist(self, col_name) -> pd.DataFrame:
        df = self.database.get_codelist(col_name)
        #TODO: subset for file
        return df

    def get_ddic(self, refresh=False) -> ET.Element:
        """Generates an DDI-Codebook for this file.
        
        This uses the database level DDI-Codebook and strips/adjusts content.
        """
        logging.debug(f"Generating DDI-Codebook for {self.filename}")
        ddi_codebook = self.database.get_ddic(refresh)
        # adjust codeBook ID
        ddi_codebook.set("ID", f"{ddi_codebook.get('ID')}_{self.number}")
        # adjust titl
        ddi_stdyDscr_citation_titlStmt_titl = ddi_codebook.find(r"{ddi:codebook:2_5}stdyDscr/{ddi:codebook:2_5}citation/{ddi:codebook:2_5}titlStmt/{ddi:codebook:2_5}titl")
        ddi_stdyDscr_citation_titlStmt_titl.text = f"{self.topic} {ddi_stdyDscr_citation_titlStmt_titl.text}"
        # remove other fileDscr
        file_id = f"F{self.number}"
        for fileDscr in ddi_codebook.findall(r"{ddi:codebook:2_5}fileDscr"):
            if fileDscr.get("ID") != file_id:
                ddi_codebook.remove(fileDscr)
        # adjust variables
        for var in ddi_codebook.findall(r"{ddi:codebook:2_5}dataDscr/{ddi:codebook:2_5}var"):
            var.set("files", file_id) # adjust @files
            # subset catgry based on distinct values for this file
            cats = var.findall(r"{ddi:codebook:2_5}catgry")
            if cats:
                n_dropped = 0
                distinct_values = self.get_pandas_df()[var.get("name")].unique().tolist()
                for catgry in cats:
                    value = catgry.find(r"{ddi:codebook:2_5}catValu")
                    value = value.text
                    if value not in distinct_values:
                        n_dropped += 1
                        var.remove(catgry)
                if n_dropped > 0:
                    logging.debug(f"Dropped {n_dropped} categories for {var.get('name')}")
            elif var.get("name") in ["year","period_number"]:
                # generate catgry for numeric variables
                distinct_values = self.get_pandas_df()[var.get("name")].unique().tolist()
                for value in distinct_values:
                    catgry = ET.SubElement(var, "{ddi:codebook:2_5}catgry")
                    catValu = ET.SubElement(catgry, "{ddi:codebook:2_5}catValu")
                    catValu.text = str(value)
                    labl = ET.SubElement(catgry, "{ddi:codebook:2_5}labl")
                    labl.text = str(value)
        return ddi_codebook

    def get_series_ids(self):
        """Returns a list of series ids in the data file.
        """
        return self.get_pandas_df()['series_id'].unique()

    def get_series_id_time_period(self, series_id):
        """Returns the time period of the given series id.
        """
        filter = self.get_pandas_df()['series_id']==series_id
        min = self.get_pandas_df()[filter]['year_period'].min()
        max = self.get_pandas_df()[filter]['year_period'].max()
        return (min,max)

    @cache
    def get_time_period(self):
        """Returns the time period of the data file.
        """
        min = self.get_pandas_df()['year_period'].min()
        max = self.get_pandas_df()['year_period'].max()
        return (min,max)

    def to_ddic(self):
        """Saves DDI-Codebook for the file."""
        ET.register_namespace('', 'ddi:codebook:2_5')
        tree = ET.ElementTree(self.get_ddic(refresh=True))
        tree.write(self.ddic_filepath, encoding="utf-8", xml_declaration=True)


class BlsMappingFile(BlsFile):
    def __init__(self, database, name):
        super().__init__(database, name)

class BlsSeriesFile(BlsFile):
    _pandas_df = None

    def __init__(self, database, name):
        super().__init__(database, name) 

    def get_ddic(self, refresh=False) -> ET.Element:
        """Returns the DDI-Codebook for this data file.
        """
        ddi_codebook = self.database.get_ddi_codebook()
        return ddi_codebook

    def get_pandas_df(self, refresh=False, from_parquet=False):
        """Returns the Pandas DataFrame for this data file.
        Loads the CSV data, applies various cleansing steps, and computes derived variables.
        If from_parquet is True, the dataframe is loaded from the parquet file instead.
        """
        if os.path.isfile(self.filepath):
            if self._pandas_df is None or refresh:
                if os.path.isfile(self.parquet_filepath) and from_parquet:
                    logging.debug(f"Loading {self.parquet_filepath}")
                    self._pandas_df = pd.read_parquet(self.parquet_filepath)
                else: # load from BLS data file
                    logging.debug(f"Loading {self.filepath}")
                    # load from raw CSV (all columns as string)
                    self._pandas_df = pd.read_csv(self.filepath, delimiter="\t", dtype=str, low_memory=False)
                    # remove spaces from column names
                    self._pandas_df.columns = self._pandas_df.columns.str.strip()
                    # remove spaces from series_id values
                    self._pandas_df['series_id'] = self._pandas_df['series_id'].str.strip()
                    # hard patch for known issues
                    if self.database.id == 'ce':
                        logging.debug("Patching ce.series columns")
                        self._pandas_df = self._pandas_df.rename(columns={
                            'data_type_code': 'datatype_code'
                        })
                    elif self.database.id == 'ep':
                        logging.debug("Patching ep.series columns")
                        self._pandas_df = self._pandas_df.rename(columns={
                            'disp_code': 'display_code',
                            'ind_code': 'industry_code',
                            'occ_code': 'occupation_code',
                        })
                    elif self.database.id == 'ip':
                        logging.debug("Patching ip.series columns")
                        self._pandas_df = self._pandas_df.rename(columns={
                            'seasonal': 'seasonal_code'
                        })
        return self._pandas_df

class BlsTxtFile(BlsFile):
    _sections: list[str]
    def __init__(self, database, name):
        super().__init__(database, name)
        self.load()

    @property
    def sections(self) -> list[str]:
        return self._sections
    

    @property
    def description(self):
        """Section 1: description of the database.
        
        This is just a block of text that can be returned as-is.

        It could be further parsed to extracts information on specific topics 
        which are paragraphs that start witn <topic>: 
        (e.g. Frequency of Observations, Annual Averages, ...)

        """
        return self._sections[1]

    def load(self):
        self._sections = []
        current_section = 0
        self._sections.append('')
        with open(self.filepath, 'r', encoding='utf-8', errors='replace') as file:
            try:
                while True:
                    line = next(file)
                    if line.startswith("====="):
                        current_section += 1
                        self._sections.append('')
                        line = next(file) # section
                        line = next(file) # ====
                        line = next(file)
                    self._sections[current_section] += line
            except StopIteration:
                pass

        