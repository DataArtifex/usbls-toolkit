"""
python documenter.py overview
python documenter.py sync
"""


from datetime import datetime, timedelta
from dartfx.usbls import model
import logging
import argparse
import os
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level="DEBUG")

def overview(repository, mdfile):
    mdfile.writelines([
        "# BLS Repository Overview\n",
        f"Report Date: {datetime.now().strftime('%Y-%m-%d')}\n\n",
        "\n"
    ])


    mdfile.write("| Id | Name | #Files | Local updated |\n")
    mdfile.write("|----|------|--------|---------------|\n")
    for db_id,props in model.DATABASES.items():
        db = model.BlsDatabase(repository, db_id)
        mdfile.write(f"| {db_id} | {db.name} | {len(db.files)} | {db.files_updated_range[1] if db.files_updated_range else 'N/A'} |\n")

    for db_id,props in model.DATABASES.items():
        db = model.BlsDatabase(repository, db_id)
        mdfile.write(f"## {db_id}: {props.get('name')} \n\n")

        mdfile.write("| Property | Value |\n")
        mdfile.write("|----------|-------|\n")
        mdfile.write(f"| Source | <a href='{db.bls_url}' target='_blank'>{db.bls_url}</a> |\n")
        mdfile.write(f"| Repository | {db.bls_dir} |\n")
        mdfile.write(f"| Series ID Pattern | `{db.series_id_pattern}` |\n")
        mdfile.write(f"| # Files | {len(db.files)} |\n")
        mdfile.write(f"| # Size | {db.size_formatted} |\n")
        if db.files_updated_range:
            mdfile.write(f"| Last Updated | {db.files_updated_range[1]}|\n")
        mdfile.write("\n\n")

        
        mdfile.write("### Files\n\n")
        mdfile.write("| File | Type | Size | Updated |\n")
        mdfile.write("|------|------|------|--------|\n")
        for filename, file in db.files.items():
            mdfile.write(f"| {filename} | {file.__class__.__name__} | <span style='white-space: nowrap'>{file.size_formatted}</span> | <span style='white-space: nowrap'>{file.updated}</span> |\n")

    pass

def db_report(repository, mdfile, db):
    mdfile.writelines([
        f"## {db.id}: {db.name}\n"
    ])
    mdfile.write("### Series\n\n")    
    df = db.seriesfile.get_pandas_df()
    mdfile.write(df.describe().to_markdown())
    pass

def db_series_report(repository, mdfile, db):

    # private helper to render a codefile to markdown 
    # (used for both ID components and series attributes)
    def codefile_to_md(codefile: model.BlsCodeFile):
        codefile_df = codefile.get_pandas_df() if codefile else None       
        mdfile.write("| Property | Value |\n")
        mdfile.write("|----------|-------|\n")
        mdfile.write(f"| filename | {codefile.filename}|\n")
        mdfile.write(f"| size | {codefile.size_formatted}|\n")
        mdfile.write(f"| #codes | {codefile_df.shape[0]:,}|\n")
        mdfile.write(f"| variables | {', '.join(codefile_df.columns.tolist())}|\n")
        mdfile.write("\n\n")
        # show codes
        max_codes = args.ncodes if hasattr(args, 'ncodes') else 20
        mdfile.write("#### Codes\n\n")
        mdfile.write("| Value | Label |\n")
        mdfile.write("|-------|-------|\n")
        for index, row in codefile.codelist.head(max_codes).iterrows():
            value = row.iloc[0]
            label = row.iloc[1]
            mdfile.write(f"| {value} | {label} |\n")
        if codefile.codelist.shape[0] > max_codes:
            remaining_codes = codefile.codelist.shape[0] - max_codes
            mdfile.write(f"| ... | {remaining_codes} more codes |\n")
        mdfile.write("\n\n")


    mdfile.writelines([
        f"# {db.id}: {db.name}\n\n"
    ])
    mdfile.write(f"Report Date: {datetime.now().strftime('%Y-%m-%d')}\n\n")

    series_df = db.seriesfile.get_pandas_df()

    #mdfile.write("## Overview\n\n")
    #mdfile.write("@TODO\n\n")
    #mdfile.write("\n\n")

    ## SERIES FILE
    mdfile.write("## Series File\n\n")
    mdfile.write("| Property | Value |\n")
    mdfile.write("|----------|-------|\n")
    mdfile.write(f"| filename | {db.seriesfile.filename}|\n")
    mdfile.write(f"| size | {db.seriesfile.size_formatted}|\n")
    mdfile.write(f"| #series | {series_df.shape[0]:,}|\n")
    mdfile.write(f"| #attributes | {series_df.columns.shape[0]}|\n")
    mdfile.write(f"| variables | {', '.join(series_df.columns.tolist())}|\n")
    mdfile.write("\n\n")
    mdfile.write("### Variables\n\n")
    mdfile.write(f"Variables in the {db.id}.series file\n\n")
    mdfile.write("| column | count | unique | top | frequency |\n")
    mdfile.write("|--------|-------|--------|-----|-----------|\n")
    for column in series_df.describe().columns:
        top_value = series_df[column].mode().iloc[0] if not series_df[column].mode().empty else "N/A"
        top_freq = series_df[column].value_counts().iloc[0] if not series_df[column].value_counts().empty else 0
        mdfile.write(f"| {column} | {series_df[column].count()} | {series_df[column].nunique()} | {top_value} | {top_freq} |\n")
    mdfile.write("\n\n")

    ## ID COMPONENTS
    mdfile.write("## Series ID Components\n\n")
    components = db.get_series_components()
    mdfile.write("| Name | Class | Length | Regex |\n")
    mdfile.write("|----------|-------|--------|-------|\n")
    for component in components:
        mdfile.write(f"| {component['name']} | `{component['class']}` | `{component['length']}` | `{component['pattern']}` |\n")
    mdfile.write("\n\n")

    ### SERIES ID CODES
    mdfile.write("### Component Codes\n\n")
    mdfile.write("Code lists and attributes for series components\n\n")
    mdfile.write("\n\n")
    for component in components:
        component_name = component['name']
        # skip database_id
        if component_name == 'database_id':
            continue
        mdfile.write(f"### {component['name']}\n\n")
        # get the matching code file
        codefile = db.get_codefile(component_name)
        # render codefile
        if codefile:
            codefile_to_md(codefile)
        else:
            logging.warning(f"No code file found for: {component_name} in database {db.id}")
            mdfile.write("Codes file/list not available.\n\n")

    ## OTHER ATTRIBUTES
    mdfile.write("## Series Attributes\n\n")
    attributes = db.get_series_attributes()

    mdfile.write("| Name | Type |\n")
    mdfile.write("|------|------|\n")
    for attribute in attributes:
        mdfile.write(f"| {attribute['name']} | `{attribute['type']}`|\n")
    mdfile.write("\n\n")

    for attribute in attributes:
        mdfile.write(f"### {attribute['name']} ({attribute['type']})\n\n")
        attribute_name = attribute['name']
        attribute_type = attribute['type']
        if attribute_type == 'code':
            codefile = db.get_codefile(attribute_name)
            if codefile:
                codefile_to_md(codefile)
            else:
                logging.warning(f"No code file found for attribute {attribute_name} in database {db.id}")
                mdfile.write("Codes file/list not available.\n\n")
        elif attribute_type == 'time':
            freqs = series_df[attribute_name].value_counts().sort_index()
            mdfile.write("| Value | Count |\n")
            mdfile.write("|-------|-------|\n")
            for value, count in freqs.items():
                mdfile.write(f"| {value} | {count} |\n")
            mdfile.write("\n\n")
        else:
            mdfile.write("No additional information available.\n\n")
            mdfile.write("\n\n")

def sync_report(repository, mdfile):
    mdfile.writelines([
        "# BLS Repository Sync Report\n",
        f"Report Date: {datetime.now().strftime('%Y-%m-%d')}\n",
        "\n"
    ])

    outdated_databases = 0
    aging_databases = 0
    inactive_databases = 0


    table_rows = ""
    for db_id in model.DATABASES:
        status = []
        db = model.BlsDatabase(repository, db_id)
        bls_updated = db.files_bls_updated_range[1] if db.files_bls_updated_range else None
        repository_updated = db.files_updated_range[1] if db.files_updated_range else None

        bls_style = []        
        repository_style = []

        if not bls_updated or not repository_updated:
            continue

        if bls_updated < datetime.now() - timedelta(days=365*4):
            bls_style.append("color:red")
            bls_style.append("font-weight:bold")
            inactive_databases += 1
            status.append('inactive')
        elif bls_updated < datetime.now() - timedelta(days=365*2):
            bls_style.append("color:orange")
            aging_databases += 1
            status.append('aging')  
        else:
            bls_style.append("color:green")
            status.append('active')
        
        if bls_updated > repository_updated:
            repository_style.append("color:red")
            repository_style.append("font-weight:bold")
            outdated_databases += 1
            status.append('out-of-sync')
        else:
            status.append('in-sync')
            repository_style.append("color:green")

        bls_style.append("white-space: nowrap")
        repository_style.append("white-space: nowrap")

        bls_css = "style='" + "; ".join(bls_style) + "'"
        repository_css = "style='" + "; ".join(repository_style) + "'"

        table_rows += f"| {db_id} | {db.name} | {len(db.files)} | <span style='white-space: nowrap'>{db.size_formatted}</span> | {', '.join(status)} |<span {bls_css}>{bls_updated.strftime('%Y-%m-%d')}</span> |  <span {repository_css}>{repository_updated.strftime('%Y-%m-%d')}</span> |\n"


    mdfile.write(f"- Total Databases: {len(model.DATABASES)}\n")
    mdfile.write(f"- Outdated Databases: {outdated_databases}\n")
    mdfile.write(f"- Aging Databases: {aging_databases} (2+ years since last update)\n")
    mdfile.write(f"- Inactive Databases: {inactive_databases} (4+ years since last update)\n")
    mdfile.write("\n\n")

    mdfile.write("| Id | Name | #Files | Size | Status | BLS updated | Local updated |\n")
    mdfile.write("|----|------|--------|------|--------|-------------|---------------|\n")
    mdfile.write(table_rows)


def main(repository, mdfile):
    databases = model.DATABASES.keys()
    for db in databases:
        db = model.BlsDatabase(repository, db)

#
# MAIN
#
if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(script_dir, '..', 'reports')
    
    # Ensure reports directory exists
    os.makedirs(reports_dir, exist_ok=True)
    
    parser = argparse.ArgumentParser(description='Generate BLS database reports')
    
    # General arguments that apply to all reports
    parser.add_argument('-r','--repository', default='/data/us-bls/repository', help='Path to BLS repository')
    parser.add_argument('-db', '--database', help='Database name (required for database-specific reports)')
    
    # Subparsers for different report types
    subparsers = parser.add_subparsers(dest='report', help='Report type')

    # Overview report
    overview_parser = subparsers.add_parser('overview', help='Generate overview report')
    overview_parser.add_argument('-o','--output', default=os.path.join(reports_dir, 'bls_db_overview.md'), help='Output markdown file')

    # Sync report
    sync_parser = subparsers.add_parser('sync', help='Generate sync report')
    sync_parser.add_argument('-o','--output', default=os.path.join(reports_dir, 'bls_db_sync.md'), help='Output markdown file')

    # Database report
    db_parser = subparsers.add_parser('db', help='Generate database report')
    db_parser.add_argument('database', help='Database identifier')

    # Database series report
    db_parser = subparsers.add_parser('series', help='Generate database series report')
    db_parser.add_argument('database', help='Database identifier')
    db_parser.add_argument('--ncodes', default=20, type=int, help='Number of codes to display per component (default: 20)')

    # Parse arguments
    args = parser.parse_args()

    # Validate arguments based on report type
    if args.report == 'db' and not args.database:
        parser.error("Database report requires --database argument")

    # Create repository object
    repository = model.BlsRepository(args.repository)

    # Execute the appropriate report
    if args.report == 'overview':
        with open(args.output, 'w', encoding='utf-8') as mdfile:
            overview(repository, mdfile)
    elif args.report == 'db':
        db = model.BlsDatabase(repository, args.database)
        db_output_path = os.path.join(reports_dir, f'bls_db_{args.database}.md')
        with open(db_output_path, 'w', encoding='utf-8') as mdfile:
            db_report(repository, mdfile, db)
    elif args.report == 'sync':
        with open(args.output, 'w', encoding='utf-8') as mdfile:
            sync_report(repository, mdfile)
    elif args.report == 'series':
        if args.database in ['*','all']:
            # use all databases that have a series_id_pattern
            db_ids = []
            for id,database in model.DATABASES.items():
                if database.get('series_id_pattern'):
                    db_ids.append(id)
        else:
            # assume this is a single or comma-separated list of database ids
            db_ids = args.database.split(",")
        # run report for each database
        print(db_ids)
        for db_id in db_ids:
            print(f"Generating series report for database: {db_id}")
            db = model.BlsDatabase(repository, db_id)
            series_output_path = os.path.join(reports_dir, f'bls_db_{db_id}_series.md')
            with open(series_output_path, 'w', encoding='utf-8') as mdfile:
                db_series_report(repository, mdfile, db)
    else:
        parser.print_help()
