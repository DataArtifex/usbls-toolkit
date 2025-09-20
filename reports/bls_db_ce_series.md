# ce: Employment, Hours, and Earnings-National (NAICS)

Report Date: 2025-09-19

## Series File

| Property | Value |
|----------|-------|
| filename | ce.series|
| size | 3.76 MB|
| #series | 22,049|
| #attributes | 11|
| variables | series_id, supersector_code, industry_code, datatype_code, seasonal, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the ce.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 22049 | 22049 | CES0000000001 | 1 |
| supersector_code | 22049 | 22 | 31 | 3096 |
| industry_code | 22049 | 850 | 30000000 | 63 |
| datatype_code | 22049 | 41 | 01 | 1692 |
| seasonal | 22049 | 2 | S | 11027 |
| series_title | 22049 | 22049 | Aggregate weekly hours of all employees, thousands, accommodation and food services, not seasonally adjusted | 1 |
| footnote_codes | 8272 | 1 | I | 8272 |
| begin_year | 22049 | 21 | 1990 | 10418 |
| begin_period | 22049 | 4 | M01 | 11723 |
| end_year | 22049 | 1 | 2025 | 22049 |
| end_period | 22049 | 3 | M07 | 20191 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| industry_code | `\d` | `8` | `?P<industry_code>[\d]{8}` |
| datatype_code | `\d` | `4` | `?P<datatype_code>[\d]{4}` |


### Component Codes

Code lists and attributes for series components



### industry_code

| Property | Value |
|----------|-------|
| filename | ce.industry|
| size | 57.39 KB|
| #codes | 850|
| variables | industry_code, naics_code, publishing_status, industry_name, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 0 | Total nonfarm |
| 5000000 | Total private |
| 6000000 | Goods-producing |
| 7000000 | Service-providing |
| 8000000 | Private service-providing |
| 10000000 | Mining and logging |
| 10113300 | Logging |
| 10210000 | Mining, quarrying, and oil and gas extraction |
| 10211000 | Oil and gas extraction |
| 10212000 | Mining (except oil and gas) |
| 10212100 | Coal mining |
| 10212114 | Surface coal mining |
| 10212115 | Underground coal mining |
| 10212200 | Metal ore mining |
| 10212220 | Gold ore and silver ore mining |
| 10212290 | Iron ore, copper, nickel, lead, zinc, and other metal ore mining |
| 10212300 | Nonmetallic mineral mining and quarrying |
| 10212310 | Stone mining and quarrying |
| 10212312 | Crushed and broken limestone mining and quarrying |
| 10212319 | Dimension stone, crushed and broken granite, and other crushed and broken stone mining and quarrying |
| ... | 830 more codes |


### datatype_code

| Property | Value |
|----------|-------|
| filename | ce.datatype|
| size | 2.45 KB|
| #codes | 41|
| variables | datatype_code, datatype_text|


#### Codes

| Value | Label |
|-------|-------|
| 01 | ALL EMPLOYEES, THOUSANDS |
| 02 | AVERAGE WEEKLY HOURS OF ALL EMPLOYEES |
| 03 | AVERAGE HOURLY EARNINGS OF ALL EMPLOYEES |
| 04 | AVERAGE WEEKLY OVERTIME HOURS OF ALL EMPLOYEES |
| 06 | PRODUCTION AND NONSUPERVISORY EMPLOYEES, THOUSANDS |
| 07 | AVERAGE WEEKLY HOURS OF PRODUCTION AND NONSUPERVISORY EMPLOYEES |
| 08 | AVERAGE HOURLY EARNINGS OF PRODUCTION AND NONSUPERVISORY EMPLOYEES |
| 09 | AVERAGE WEEKLY OVERTIME HOURS OF PRODUCTION AND NONSUPERVISORY EMPLOYEES |
| 10 | WOMEN EMPLOYEES, THOUSANDS |
| 11 | AVERAGE WEEKLY EARNINGS OF ALL EMPLOYEES |
| 12 | AVERAGE WEEKLY EARNINGS OF ALL EMPLOYEES, 1982-1984 DOLLARS |
| 13 | AVERAGE HOURLY EARNINGS OF ALL EMPLOYEES, 1982-1984 DOLLARS |
| 15 | AVERAGE HOURLY EARNINGS OF ALL EMPLOYEES, EXCLUDING OVERTIME |
| 16 | INDEXES OF AGGREGATE WEEKLY HOURS OF ALL EMPLOYEES, 2007=100 |
| 17 | INDEXES OF AGGREGATE WEEKLY PAYROLLS OF ALL EMPLOYEES, 2007=100 |
| 19 | AVERAGE WEEKLY HOURS OF ALL EMPLOYEES, QUARTERLY AVERAGES |
| 20 | AVERAGE WEEKLY OVERTIME HOURS OF ALL EMPLOYEES, QUARTERLY AVERAGES |
| 21 | DIFFUSION INDEXES, 1-MONTH SPAN |
| 22 | DIFFUSION INDEXES, 3-MONTH SPAN |
| 23 | DIFFUSION INDEXES, 6-MONTH SPAN |
| ... | 21 more codes |


## Series Attributes

| Name | Type |
|------|------|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| seasonal | `other`|
| series_title | `text`|
| supersector_code | `code`|


### begin_period (time)

| Value | Count |
|-------|-------|
| M01 | 11723 |
| M03 | 10320 |
| M04 | 3 |
| M06 | 3 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1939 | 108 |
| 1947 | 54 |
| 1951 | 18 |
| 1955 | 12 |
| 1956 | 25 |
| 1958 | 48 |
| 1959 | 12 |
| 1960 | 10 |
| 1964 | 259 |
| 1968 | 20 |
| 1972 | 488 |
| 1975 | 4 |
| 1976 | 58 |
| 1981 | 3 |
| 1982 | 154 |
| 1985 | 26 |
| 1990 | 10418 |
| 1991 | 8 |
| 2001 | 12 |
| 2006 | 10311 |
| 2009 | 1 |


### end_period (time)

| Value | Count |
|-------|-------|
| M06 | 13 |
| M07 | 20191 |
| M08 | 1845 |


### end_year (time)

| Value | Count |
|-------|-------|
| 2025 | 22049 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | ce.footnote|
| size | 0.15 KB|
| #codes | 3|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| C | corrected |
| I | Seasonally Adjusted Independently. See www.bls.gov/opub/hom/ces/calculation.htm for details. |
| P | preliminary |


### seasonal (other)

No additional information available.



### series_title (text)

No additional information available.



### supersector_code (code)

| Property | Value |
|----------|-------|
| filename | ce.supersector|
| size | 0.54 KB|
| #codes | 22|
| variables | supersector_code, supersector_name|


#### Codes

| Value | Label |
|-------|-------|
| 0 | Total nonfarm |
| 5 | Total private |
| 6 | Goods-producing |
| 7 | Service-providing |
| 8 | Private service-providing |
| 10 | Mining and logging |
| 20 | Construction |
| 30 | Manufacturing |
| 31 | Durable Goods |
| 32 | Nondurable Goods |
| 40 | Trade, transportation, and utilities |
| 41 | Wholesale trade |
| 42 | Retail trade |
| 43 | Transportation and warehousing |
| 44 | Utilities |
| 50 | Information |
| 55 | Financial activities |
| 60 | Professional and business services |
| 65 | Private education and health services |
| 70 | Leisure and hospitality |
| ... | 2 more codes |


