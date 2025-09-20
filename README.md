# US Bureau of Labor Statistics (BLS) Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Development Status](https://img.shields.io/badge/status-early%20release-orange.svg)](https://github.com/DataArtifex/usbls-toolkit)

---

**Table of Contents**

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command Line Tools](#command-line-tools)
- [API Usage](#api-usage)
- [Supported Databases](#supported-databases)
- [Examples](#examples)
- [Development](#development)
- [License](#license)

## Overview

The **US BLS Toolkit** is a experimental Python utility library for working with databases from the U.S. Bureau of Labor Statistics (BLS). This toolkit provides easy-to-use interfaces for downloading, processing, analyzing, and generating reports from BLS time series data.

### Objectives

The toolkit addresses key challenges in working with BLS data by focusing on five main objectives:

- **🤖 Machine Actionability & AI Friendliness**: Transform BLS data into formats and structures that are easily consumable by automated systems, machine learning models, and AI applications
- **📚 Digital Knowledge Generation**: Create comprehensive metadata and documentation around BLS datasets, making implicit knowledge explicit and discoverable
- **🔍 Time Series Discovery**: Solve the significant challenge of finding the right time series data among the thousands available in BLS databases - a major pain point for researchers and analysts
- **🔌 API Implementation**: Facilitate the implementation of APIs by providing structured data access patterns and standardized interfaces for BLS datasets
- **📈 Enhanced Usability & FAIR Principles**: Improve overall usability of BLS datasets while aligning with global initiatives such as [FAIR data principles](https://https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, and Reusable) or [Cross-Domain Data Interoperability Framework (CDIF)](https://cdif.codata.org)

> **Note**: This is an early release version. APIs and functionality subject to change.

## Features

- 🔄 **Data Harvesting**: Automatically download and sync BLS data files to a local repository
- 📊 **Data Processing**: Convert BLS data to common formats (CSV, Parquet, Pandas DataFrames)
- 📈 **Analysis Tools**: Built-in statistical analysis and data exploration capabilities
- 📋 **Report Generation**: Generate comprehensive markdown reports on database status and contents
- 🏷️ **Metadata Support**: Extract and work with BLS series metadata and code lists
- 🔍 **Database Discovery**: Explore available BLS databases and their characteristics
- 🐍 **Python Integration**: Native pandas and Spark DataFrame support
- 📝 **DDI Support**: Generate DDI-Codebook metadata for datasets

### Data Harvesting

The toolkit creates a local repository of BLS data by downloading raw data files from the Bureau of Labor Statistics website. The harvesting process is intelligent:

- **Initial Download**: Downloads all available files for selected databases
- **Incremental Sync**: Subsequent runs only download files that have been updated since the last harvest
- **Size & Date Verification**: Compares file sizes and modification dates to determine what needs updating
- **Selective Harvesting**: Choose to harvest all databases or specific ones

#### Harvesting Example

```python
from dartfx.usbls import model
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level="DEBUG")

# Initialize local repository
repo = model.BlsRepository('/path/to/your/bls/repository')

# Harvest all databases
databases = model.DATABASES.keys()  # all available databases
# Or harvest specific databases only:
# databases = ['cu', 'cw', 'ce']  # CPI and employment data only

for database in databases:
    print(f"Harvesting database: {database}")
    db = model.BlsDatabase(repo, database)
    db.harvest()  # Downloads only new/changed files
```

This approach ensures you maintain a complete, up-to-date local copy of BLS data while minimizing bandwidth usage and download time.

### Supported Data Formats

- **Input**: BLS native tab-delimited files
- **Output**: CSV, Parquet, Pandas DataFrame, Spark DataFrame
- **Metadata**: DDI-Codebook XML, JSON

## Installation

> **Note**: This package is not yet published on PyPI. Until the official release, please install locally using the development installation method below.

### Local Installation (Current Method)

```bash
git clone https://github.com/DataArtifex/usbls-toolkit
cd usbls-toolkit
pip install -e .
```

### Future PyPI Installation

Once published on PyPI, you will be able to install using:

```bash
pip install dartfx-usbls
```

## Getting Started

The BLS Toolkit works with a **local repository** approach - you create a local copy of BLS data that can be efficiently synced and analyzed. Here's how to get started:

### Step 1: Create a Local Repository

First, decide where you want to store your BLS data repository. This should be a location with sufficient disk space, as BLS databases can be quite large (~40Gb).

```python
from dartfx.usbls import model
import logging

# Set up logging to see the harvesting progress
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level="INFO")

# Initialize your local BLS repository
repo = model.BlsRepository('/path/to/your/bls/repository')
```

### Step 2: Harvest BLS Data

The harvesting process downloads raw data files from the BLS website to your local repository. You can harvest all databases or select specific ones:

#### Option A: Harvest All Databases
```python
# Harvest all available BLS databases (58 databases)
databases = model.DATABASES.keys()  

for database in databases:
    print(f"Harvesting database: {database}")
    db = model.BlsDatabase(repo, database)
    db.harvest()  # Downloads only new/changed files
```

#### Option B: Harvest Specific Databases
```python
# Harvest only the databases you need
databases = ['cu', 'cw', 'ce', 'la']  # CPI, CPI-W, Employment, Unemployment

for database in databases:
    print(f"Harvesting database: {database}")
    db = model.BlsDatabase(repo, database)
    db.harvest()
```

### Step 3: Work with Your Data

Once harvested, you can efficiently work with the local data:

```python
# Access a specific database (e.g., Consumer Price Index)
cpi_db = model.BlsDatabase(repo, 'cu')

# Convert to pandas DataFrame (no download needed - uses local files)
df = cpi_db.datafile0.get_pandas_df()

# Explore your data
print(f"Database: {cpi_db.name}")
print(f"Records: {len(df):,}")
print(f"Series: {df['series_id'].nunique():,}")
print(f"Time period: {cpi_db.datafile0.get_time_period()}")

# Access metadata
series_df = cpi_db.seriesfile.get_pandas_df()
area_codes = cpi_db.get_codelist('area')
```

### Step 4: Keep Your Repository Updated

After the initial harvest, subsequent syncs are fast and efficient:

```python
# Re-run harvest to sync only changed files
cpi_db.harvest()  # Only downloads files that have been updated on BLS website
```

### Understanding the Process

**What happens during harvesting:**
- 🌐 Scrapes BLS website to discover available files
- 📊 Compares local vs. remote file sizes and timestamps  
- ⬇️ Downloads only new or updated files
- 📁 Organizes files in a structured local directory

**Benefits of this approach:**
- ⚡ **Fast Analysis**: Work with local files (no network delays)
- 🔄 **Efficient Sync**: Only download what's changed
- 📴 **Offline Capable**: Analyze data without internet connection
- 🗂️ **Organized**: Clean, structured file organization

### Repository Structure

Your local repository will be organized like this:
```
/your/bls/repository/
├── bls/                    # Raw BLS data files
│   ├── cu/                 # Consumer Price Index
│   │   ├── cu.data.0.Current
│   │   ├── cu.series
│   │   ├── cu.area
│   │   └── ...
│   ├── ce/                 # Employment data
│   └── ...
└── products/               # Processed/exported data
    ├── cu/
    │   ├── cu.data.0.Current.csv
    │   └── cu.data.0.Current.parquet
    └── ...
```

Now you're ready to explore the powerful features of the BLS Toolkit!

## Command Line Tools

### Database Documentation

Generate comprehensive reports about BLS databases:

```bash
# Generate overview report for all databases
python documenter.py --repository /path/to/bls/repo overview

# Generate detailed report for specific database
python documenter.py --repository /path/to/bls/repo --database cu db

# Generate sync status report
python documenter.py --repository /path/to/bls/repo sync
```

#### Report Types

- **Overview**: Summary of all available databases with file counts and update status
- **Database**: Detailed analysis of a specific database including series statistics
- **Sync**: Status report showing which databases need updates

## API Usage

### Working with Databases

```python
from dartfx.usbls import model

# Initialize repository
repo = model.BlsRepository('/path/to/bls/data')

# List all available databases
print("Available databases:", len(model.DATABASES))

# Access specific database
db = model.BlsDatabase(repo, 'cu')  # Consumer Price Index

# Get database information
print(f"Name: {db.name}")
print(f"Files: {len(db.files)}")
print(f"Size: {db.size_formatted}")
```

### Data Processing

```python
# Get data as pandas DataFrame
df = db.datafile0.get_pandas_df()

# Access series metadata
series_df = db.seriesfile.get_pandas_df()

# Get code lists
area_codes = db.get_codelist('area_code')
item_codes = db.get_codelist('item_code')

# Export to different formats
db.datafile0.to_csv()
db.datafile0.to_parquet()
```

### Data Analysis

```python
# Get database statistics
stats = db.datafile0.stats
print(f"Records: {stats['n_records']:,}")
print(f"Series: {stats['n_series']:,}")
print(f"Time period: {stats['period_from']} - {stats['period_to']}")

# Series ID pattern matching
if db.series_id_pattern:
    # Extract components from series IDs
    components = df['series_id'].str.extract(db.series_id_pattern)
    print(components.head())
```

## Supported Databases

The toolkit supports all major BLS databases including:

- **Consumer Price Index (CPI)**: `cu`, `cw`, `su`
- **Employment Statistics**: `ce`, `sm`, `la`, `ln`
- **Producer Price Index**: `wp`, `pc`
- **Employment Cost Index**: `ci`, `cm`
- **Occupational Statistics**: `oe`, `ii`, `cs`
- **And 50+ more databases**

For a complete list, see the [databases.json](src/dartfx/usbls/databases.json) configuration file.

## Examples

### Example 1: CPI Analysis

```python
from dartfx.usbls import model

# Setup
repo = model.BlsRepository('/path/to/bls/data')
cpi = model.BlsDatabase(repo, 'cu')

# Get all urban CPI data
df = cpi.datafile0.get_pandas_df()

# Filter for All Items, U.S. City Average
all_items = df[df['series_id'] == 'CUUR0000SA0']

# Calculate annual inflation rate
annual = all_items[all_items['period'] == 'M12']  # December values
annual['inflation_rate'] = annual['value'].pct_change() * 100

print(annual[['year', 'value', 'inflation_rate']].tail())
```

### Example 2: Employment Data

```python
# Access employment data
emp = model.BlsDatabase(repo, 'ce')
df = emp.datafile0.get_pandas_df()

# Get total nonfarm employment
total_emp = df[df['series_id'] == 'CES0000000001']
print(f"Latest employment: {total_emp['value'].iloc[-1]:,}")
```

### Example 3: Batch Processing

```python
# Process multiple databases
databases = ['cu', 'ce', 'wp']

for db_id in databases:
    db = model.BlsDatabase(repo, db_id)
    print(f"\nProcessing {db.name}...")
    
    # Harvest latest data
    db.harvest()
    
    # Export to CSV
    if db.datafile0:
        db.datafile0.to_csv()
        print(f"  Exported {db.datafile0.stats['n_records']} records")
```

## Development

### Setting up Development Environment

```bash
git clone https://github.com/DataArtifex/usbls-toolkit
cd usbls-toolkit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest coverage mypy
```

### Running Tests

```bash
# Run tests
pytest

# Run tests with coverage
coverage run -m pytest
coverage report
```

### Project Structure

```
usbls-toolkit/
├── src/dartfx/usbls/          # Main package
│   ├── __init__.py
│   ├── model.py               # Core data models
│   ├── databases.json         # Database configurations
│   └── clickhouse.py          # ClickHouse integration
├── labs/                      # Examples and tools
│   ├── documenter.py          # Report generation tool
│   └── *.ipynb               # Jupyter notebooks
├── tests/                     # Test suite
├── pyproject.toml            # Project configuration
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is not officially affiliated with the U.S. Bureau of Labor Statistics. It is an independent toolkit for working with publicly available BLS data.

## Support

- **Issues**: [GitHub Issues](https://github.com/DataArtifex/usbls-toolkit/issues)
- **Documentation**: [Project Documentation](https://github.com/DataArtifex/usbls-toolkit#readme)
- **Email**: pascal@codata.org

---

**Early Release Notice**: This is version 0.0.1 and considered an early release. APIs may change in future versions. Please pin to specific versions in production use.