# ip: Industry Productivity and Costs

Report Date: 2025-09-22

## Series File

| Property | Value |
|----------|-------|
| filename | ip.series|
| size | 3.80 MB|
| #series | 21,186|
| #attributes | 15|
| variables | series_id, seasonal_code, sector_code, industry_code, measure_code, duration_code, base_year, type_code, area_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the ip.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 21186 | 21186 | IPUAN1111__L010000000 | 1 |
| seasonal_code | 21186 | 1 | U | 21186 |
| sector_code | 21186 | 21 | E | 9538 |
| industry_code | 21186 | 778 | N______ | 1980 |
| measure_code | 21186 | 38 | L01 | 1664 |
| duration_code | 21186 | 2 | 0 | 10593 |
| base_year | 21186 | 2 | - | 14282 |
| type_code | 21186 | 6 | R | 9603 |
| area_code | 21186 | 56 | 000000 | 19206 |
| series_title | 21186 | 18841 | Annual percent change of employment for NAICS 111, crop production, U.S. total | 2 |
| footnote_codes | 0 | 0 | N/A | 0 |
| begin_year | 21186 | 14 | 1987 | 9259 |
| begin_period | 21186 | 1 | A01 | 21186 |
| end_year | 21186 | 3 | 2024 | 15112 |
| end_period | 21186 | 1 | A01 | 21186 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| sector_code | `A-Z` | `1` | `?P<sector_code>[A-Z]{1}` |
| industry_code | `A-Z0-9\_` | `7` | `?P<industry_code>[A-Z0-9\_]{7}` |
| measure_code | `A-Z0-9` | `3` | `?P<measure_code>[A-Z0-9]{3}` |
| duration_code | `\d` | `1` | `?P<duration_code>[\d]{1}` |
| area_code | `\d` | `6` | `?P<area_code>[\d]{6}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | ip.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### sector_code

| Property | Value |
|----------|-------|
| filename | ip.sector|
| size | 0.64 KB|
| #codes | 21|
| variables | sector_code, sector_text|


#### Codes

| Value | Label |
|-------|-------|
| A | Agriculture, Forestry, Fishing and Hunting |
| B | Mining |
| C | Utilities |
| D | Construction |
| E | Manufacturing |
| G | Wholesale Trade |
| H | Retail Trade |
| I | Transportation and Warehousing |
| J | Information |
| K | Finance and Insurance |
| L | Real Estate and Rental and Leasing |
| M | Professional, Scientific, and Technical Services |
| O | Management of Companies and Enterprises |
| P | Administrative and Support and Waste Management and Remediation Services |
| Q | Educational Services |
| R | Health Care and Social Assistance |
| S | Arts, Entertainment, and Recreation |
| T | Accommodation and Food Services |
| U | Other Services (except Public Administration) |
| W | Government |
| ... | 1 more codes |


### industry_code

| Property | Value |
|----------|-------|
| filename | ip.industry|
| size | 45.08 KB|
| #codes | 806|
| variables | industry_code, naics_code, industry_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| D11____ | Agriculture, forestry, fishing, and hunting |
| D21____ | Mining |
| D22____ | Utilities |
| D23____ | Construction |
| D31_33_ | Manufacturing |
| D42____ | Wholesale trade |
| D44_45_ | Retail trade |
| D48_49_ | Transportation and warehouseing |
| D512___ | Motion picture and sound recording industries |
| D517___ | Telecommunications |
| D51____ | Information |
| D52____ | Finance and insurance |
| D53____ | Real estate and rental and leasing |
| D54192_ | Photographic Services |
| D54____ | Professional, scientific, and technical services |
| D55____ | Management of companies and enterprises |
| D5613__ | Employment services |
| D5617__ | Services to buildings and dwellings |
| D56____ | Administrative and support and waste management and remediation services |
| D61____ | Educational services |
| ... | 786 more codes |


### measure_code

| Property | Value |
|----------|-------|
| filename | ip.measure|
| size | 2.06 KB|
| #codes | 38|
| variables | measure_code, measure_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| C00 | Capital productivity (Index, 2017=100) |
| C01 | Capital input (Index, 2017=100) |
| C02 | Capital costs (Millions of current dollars) |
| C03 | Capital share (Percentage) |
| C06 | Capital intensity (Index, 2017=100) |
| C07 | Contribution of capital intensity to labor productivity (Index, 2017=100) |
| L00 | Labor productivity (Index, 2017=100) |
| L01 | Hours worked (Index, 2017=100) |
| L02 | Labor compensation (Millions of current dollars) |
| L03 | Labor share (Percentage) |
| L06 | Real labor compensation (Million $) |
| L07 | Real labor compensation (Index, 2017=100) |
| L20 | Hours worked (Millions of hours) |
| M00 | Total factor productivity (Index, 2017=100) |
| M01 | Combined inputs (Index, 2017=100) |
| M02 | Combined inputs costs (Millions of current dollars) |
| M05 | Combined inputs price deflator (Index, 2017=100) |
| P00 | Intermediate inputs productivity (Index, 2017=100) |
| P01 | Intermediate inputs (Index, 2017=100) |
| P02 | Intermediate inputs costs (Millions of current dollars) |
| ... | 18 more codes |


### duration_code

| Property | Value |
|----------|-------|
| filename | ip.duration|
| size | 0.07 KB|
| #codes | 2|
| variables | duration_code, duration_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | Indexes or values |
| 1 | Annual percent changes |


### area_code

| Property | Value |
|----------|-------|
| filename | ip.area|
| size | 1.42 KB|
| #codes | 56|
| variables | area_code, area_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 0 | U.S. Total |
| 10000 | Alabama |
| 20000 | Alaska |
| 40000 | Arizona |
| 50000 | Arkansas |
| 60000 | California |
| 80000 | Colorado |
| 90000 | Connecticut |
| 100000 | Delaware |
| 110000 | District of Columbia |
| 120000 | Florida |
| 130000 | Georgia |
| 150000 | Hawaii |
| 160000 | Idaho |
| 170000 | Illinois |
| 180000 | Indiana |
| 190000 | Iowa |
| 200000 | Kansas |
| 210000 | Kentucky |
| 220000 | Louisiana |
| ... | 36 more codes |


## Series Attributes

| Name | Type |
|------|------|
| base_year | `time`|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| series_title | `text`|
| type_code | `code`|


### base_year (time)

| Value | Count |
|-------|-------|
| - | 14282 |
| 2017 | 6904 |


### begin_period (time)

| Value | Count |
|-------|-------|
| A01 | 21186 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1987 | 9259 |
| 1988 | 9259 |
| 1992 | 90 |
| 1993 | 103 |
| 1994 | 58 |
| 1995 | 45 |
| 1997 | 54 |
| 1998 | 54 |
| 2002 | 81 |
| 2003 | 81 |
| 2004 | 52 |
| 2005 | 52 |
| 2007 | 999 |
| 2008 | 999 |


### end_period (time)

| Value | Count |
|-------|-------|
| A01 | 21186 |


### end_year (time)

| Value | Count |
|-------|-------|
| 2022 | 6006 |
| 2023 | 68 |
| 2024 | 15112 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | ip.footnote|
| size | 0.03 KB|
| #codes | 0|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|


### series_title (text)

No additional information available.



### type_code (code)

| Property | Value |
|----------|-------|
| filename | ip.type|
| size | 0.08 KB|
| #codes | 6|
| variables | type_code, type_text|


#### Codes

| Value | Label |
|-------|-------|
| E | Employees |
| H | Hours |
| I | Index |
| P | Percent |
| R | Rate |
| Y | Currency |


