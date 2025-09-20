# BLS Toolkit Model Documentation

This document describes the core data model classes in the US BLS Toolkit, their relationships, and key features.

## Overview

The BLS Toolkit model follows a hierarchical structure that mirrors the organization of BLS data:
- **Repository** → Contains multiple databases
- **Database** → Contains multiple files 
- **Files** → Contain the actual data and metadata

## Class Hierarchy

```mermaid
classDiagram
    class BlsRepository {
        -str root_dir
        -str bls_dirname
        -str products_dirname
        -dict databases
        +bls_dir: str
        +products_dir: str
        +database_ids: list
    }
    
    class BlsDatabase {
        -BlsRepository repository
        -str id
        -dict files
        -dict bls_files
        +name: str
        +bls_url: str
        +bls_dir: str
        +series_id_pattern: str
        +harvest()
        +get_codelist(variable)
        +get_ddic()
    }
    
    class BlsFile {
        #BlsDatabase database
        #str filename
        #str extension
        #int size
        #datetime updated
        +filepath: str
        +bls_url: str
        +exists: bool
        +download()
        +to_csv()
        +to_parquet()
    }
    
    class BlsDataFile {
        -DataFrame pandas_df
        -dict stats
        +get_pandas_df()
        +get_series_ids()
        +get_time_period()
        +to_ddic()
    }
    
    class BlsSeriesFile {
        -DataFrame pandas_df
        +get_pandas_df()
        +get_ddic()
    }
    
    class BlsCodeFile {
        -DataFrame pandas_df
        +codelist: DataFrame
        +get_pandas_df()
    }
    
    class BlsContactsFile {
        
    }
    
    class BlsMappingFile {
        
    }
    
    class BlsTxtFile {
        -list sections
        +description: str
        +load()
    }
    
    BlsRepository ||--o{ BlsDatabase : contains
    BlsDatabase ||--o{ BlsFile : contains
    BlsFile <|-- BlsDataFile
    BlsFile <|-- BlsSeriesFile
    BlsFile <|-- BlsCodeFile
    BlsFile <|-- BlsContactsFile
    BlsFile <|-- BlsMappingFile
    BlsFile <|-- BlsTxtFile
```

## Core Classes

### BlsRepository

The top-level class representing a local BLS data repository.

**Purpose**: Manages the local file system structure and provides access to multiple BLS databases.

**Key Properties**:
- `root_dir`: Base directory for the repository
- `bls_dir`: Directory containing raw BLS data files
- `products_dir`: Directory for processed/converted data products
- `databases`: Dictionary of all available databases

**Key Methods**:
- Automatically creates directory structure
- Provides access to database instances
- Manages file organization

**Usage**:
```python
repo = model.BlsRepository('/path/to/bls/data')
print(f"Repository contains {len(repo.database_ids)} databases")
```

### BlsDatabase

Represents a specific BLS database (e.g., Consumer Price Index, Employment data).

**Purpose**: Manages all files and operations for a single BLS database, including data harvesting and processing.

**Key Properties**:
- `id`: Database identifier (e.g., 'cu', 'ce', 'la')
- `name`: Human-readable database name
- `bls_url`: Source URL on BLS website
- `series_id_pattern`: Regex pattern for parsing series IDs
- `files`: Dictionary of all files in the database

**Key Methods**:
- `harvest()`: Download/sync files from BLS website
- `get_codelist(variable)`: Get code list for a specific variable
- `scrape_database_files()`: Discover available files on BLS website
- `get_ddic()`: Generate DDI-Codebook metadata

**File Access Properties**:
- `datafiles`: Collection of data files
- `datafile0`: Current/primary data file
- `datafile1`: Historical/complete data file
- `seriesfile`: Series metadata file
- `codefiles`: Variable code files
- `txtfile`: Documentation file

**Usage**:
```python
cpi_db = model.BlsDatabase(repo, 'cu')
cpi_db.harvest()  # Download latest data
df = cpi_db.datafile0.get_pandas_df()
```

### BlsFile (Base Class)

Base class for all BLS file types.

**Purpose**: Provides common functionality for file operations, downloading, and format conversion.

**Key Properties**:
- `filename`: Original BLS filename
- `filepath`: Local file path
- `bls_url`: Source URL for downloading
- `size`: File size in bytes
- `updated`: Last modification timestamp
- `exists`: Whether file exists locally

**Key Methods**:
- `download()`: Download file from BLS website
- `to_csv()`: Convert to CSV format
- `to_parquet()`: Convert to Parquet format
- `refresh_stats()`: Update file metadata

### BlsDataFile

Specialized class for BLS time series data files.

**Purpose**: Handles the main data files containing time series observations.

**Key Features**:
- **Data Loading**: Loads tab-delimited BLS files into pandas DataFrames
- **Data Cleaning**: Automatic data type conversion and cleaning
- **Data Enrichment**: Adds computed columns (year_period, period_type, etc.)
- **Series ID Parsing**: Extracts components from series IDs using regex patterns
- **Statistics**: Generates comprehensive dataset statistics

**Enhanced DataFrame Columns**:
- `year_period`: Combined year-period identifier (e.g., "2023-M01")
- `period_type`: Type of period (M=Monthly, Q=Quarterly, etc.)
- `period_number`: Numeric period within year
- Series ID components (varies by database)

**Key Methods**:
- `get_pandas_df()`: Returns cleaned and enriched DataFrame
- `get_series_ids()`: List of all series in the file
- `get_time_period()`: Overall time span of the data
- `to_ddic()`: Generate file-specific DDI metadata

**Usage**:
```python
data_file = cpi_db.datafile0
df = data_file.get_pandas_df()
stats = data_file.stats
print(f"Contains {stats['n_series']} series, {stats['n_records']} records")
```

### BlsSeriesFile

Manages series metadata files (*.series).

**Purpose**: Contains descriptive information about each time series, including titles and classification codes.

**Key Features**:
- Loads series metadata as DataFrame
- Provides series titles and descriptions
- Maps series IDs to human-readable information
- Handles database-specific column name variations

### BlsCodeFile

Manages code list files (*.area, *.item, etc.).

**Purpose**: Provides lookup tables for codes used in series IDs and data.

**Key Features**:
- `codelist` property: Returns standardized 2-column DataFrame (code, description)
- Automatic column name detection
- Supports various code file formats

**Usage**:
```python
area_codes = cpi_db.get_codelist('area')
print(area_codes.head())  # Shows area codes and names
```

### BlsTxtFile

Manages documentation files (*.txt).

**Purpose**: Contains human-readable documentation about the database structure and contents.

**Key Features**:
- Parses structured text files into sections
- `description` property: Database overview text
- Provides detailed documentation for data elements and structure

## Data Flow and Relationships

### 1. Repository Initialization
```python
repo = model.BlsRepository('/path/to/data')
```
- Creates directory structure
- Loads database configuration from `databases.json`

### 2. Database Access
```python
db = model.BlsDatabase(repo, 'cu')
```
- Validates database ID against configuration
- Creates database-specific directories
- Initializes file discovery

### 3. File Discovery
```python
files = db.files
```
- Scans local directory for BLS files
- Creates appropriate file type instances based on extensions
- Provides typed access (datafiles, codefiles, etc.)

### 4. Data Harvesting
```python
db.harvest()
```
- Scrapes BLS website for available files
- Compares local vs. remote file timestamps/sizes
- Downloads only new or updated files

### 5. Data Processing
```python
df = db.datafile0.get_pandas_df()
```
- Loads raw tab-delimited data
- Applies data cleaning and type conversion
- Enriches with computed columns
- Parses series IDs using database-specific patterns

## Key Features

### Intelligent Data Loading
- **Lazy Loading**: Data is loaded only when accessed
- **Caching**: DataFrames are cached to avoid reprocessing
- **Format Options**: Support for both CSV and Parquet loading
- **Error Handling**: Graceful handling of malformed data

### Metadata Generation
- **DDI-Codebook**: Generates comprehensive metadata in DDI format
- **Statistics**: Automatic calculation of dataset statistics
- **Documentation**: Structured access to BLS documentation

### Series ID Pattern Matching
Each database has a regex pattern that extracts meaningful components from series IDs:

```python
# Example for Consumer Price Index (CPI)
pattern = r"(?P<database_id>[A-Z]{2})(?P<seasonal_code>[A-Z]{1})(?P<periodicity_code>[A-Z]{1})(?P<area_code>[A-Z0-9]{4})(?P<item_code>[A-Z0-9]*)"
```

This automatically creates new columns in the DataFrame for each component.

### Data Export Options
- **CSV**: Human-readable format
- **Parquet**: Efficient binary format
- **DDI XML**: Metadata standard for social sciences
- **Direct DataFrame Access**: For Python analysis

## Configuration

### Database Configuration (databases.json)
```json
{
  "cu": {
    "name": "Consumer Price Index - All Urban Consumers",
    "series_id_pattern": "(?P<database_id>[A-Z]{2})(?P<seasonal_code>[A-Z]{1})(?P<periodicity_code>[A-Z]{1})(?P<area_code>[A-Z0-9]{4})(?P<item_code>[A-Z0-9]*)",
    "is_supported": true
  }
}
```

### Directory Structure
```
repository/
├── bls/                    # Raw BLS files
│   ├── cu/                 # Consumer Price Index
│   │   ├── cu.data.0.Current
│   │   ├── cu.series
│   │   ├── cu.area
│   │   └── ...
│   └── ce/                 # Employment data
└── products/               # Processed outputs
    ├── cu/
    │   ├── cu.data.0.Current.csv
    │   ├── cu.data.0.Current.parquet
    │   └── cu.data.0.Current.ddi25.xml
    └── ce/
```

## Usage Patterns

### Basic Data Access
```python
# Initialize repository
repo = model.BlsRepository('/path/to/data')

# Access database
db = model.BlsDatabase(repo, 'cu')

# Get data
df = db.datafile0.get_pandas_df()

# Filter for specific series
inflation_data = df[df['series_id'] == 'CUUR0000SA0']
```

### Batch Processing
```python
# Process multiple databases
for db_id in ['cu', 'cw', 'ce']:
    db = model.BlsDatabase(repo, db_id)
    db.harvest()  # Sync latest data
    df = db.datafile0.get_pandas_df()
    print(f"{db.name}: {len(df)} records")
```

### Metadata Exploration
```python
# Explore series metadata
series_df = db.seriesfile.get_pandas_df()
print(series_df.head())

# Get code lists
area_codes = db.get_codelist('area')
item_codes = db.get_codelist('item')

# Generate documentation
db.to_ddic()  # Creates DDI-Codebook XML
```

This model provides a comprehensive, type-safe, and efficient way to work with BLS data while maintaining the flexibility to access raw files when needed.
