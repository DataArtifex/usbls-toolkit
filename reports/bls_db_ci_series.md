# ci: Employment Cost Index (NAICS)

Report Date: 2025-09-19

## Series File

| Property | Value |
|----------|-------|
| filename | ci.series|
| size | 475.77 KB|
| #series | 2,470|
| #attributes | 15|
| variables | series_id, seasonal, owner_code, industry_code, occupation_code, subcell_code, area_code, periodicity_code, estimate_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the ci.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 2470 | 2470 | CIS1010000000000I | 1 |
| seasonal | 2470 | 2 | U | 2170 |
| owner_code | 2470 | 3 | 2 | 1819 |
| industry_code | 2470 | 35 | 000000 | 1094 |
| occupation_code | 2470 | 20 | 000000 | 1338 |
| subcell_code | 2470 | 4 | 00 | 2110 |
| area_code | 2470 | 31 | 99999 | 2260 |
| periodicity_code | 2470 | 9 | I | 506 |
| estimate_code | 2470 | 4 | 01 | 1168 |
| series_title | 2470 | 2182 | (Discontinued SOC 2010) Total compensation for private industry workers in office and administrative support occupations, 3-month percent change, current dollars | 2 |
| footnote_codes | 1586 | 35 | J | 834 |
| begin_year | 2470 | 12 | 2001 | 1850 |
| begin_period | 2470 | 3 | Q01 | 2352 |
| end_year | 2470 | 6 | 2025 | 1968 |
| end_period | 2470 | 3 | Q02 | 1968 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| owner_code | `\d` | `1` | `?P<owner_code>[\d]{1}` |
| estimate_code | `\d` | `2` | `?P<estimate_code>[\d]{2}` |
| industry_code | `\d` | `4` | `?P<industry_code>[\d]{4}` |
| occupation_code | `\d` | `3` | `?P<occupation_code>[\d]{3}` |
| subcell_code | `\d` | `2` | `?P<subcell_code>[\d]{2}` |
| periodicity_code | `A-Z` | `1` | `?P<periodicity_code>[A-Z]{1}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | ci.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### owner_code

| Property | Value |
|----------|-------|
| filename | ci.owner|
| size | 0.16 KB|
| #codes | 3|
| variables | owner_code, owner_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Civilian workers |
| 2 | Private industry workers |
| 3 | State and local government workers |


### estimate_code

| Property | Value |
|----------|-------|
| filename | ci.estimate|
| size | 0.17 KB|
| #codes | 4|
| variables | estimate_code, estimate_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Total compensation |
| 2 | Wages and salaries |
| 3 | Total benefits |
| 15 | Health insurance |


### industry_code

| Property | Value |
|----------|-------|
| filename | ci.industry|
| size | 1.59 KB|
| #codes | 36|
| variables | industry_code, industry_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 000000 | All industries |
| 220000 | Utilities |
| 230000 | Construction |
| 300000 | Manufacturing |
| 310000 | Nondurable Goods manufacturers |
| 320000 | Durable Goods manufacturers |
| 336411 | Aircraft manufacturing |
| 400000 | Trade, transportation, and utilities |
| 412000 | Retail trade |
| 420000 | Wholesale trade |
| 430000 | Transportation and warehousing |
| 510000 | Information |
| 520000 | Finance and insurance |
| 520A00 | Financial activities |
| 522000 | Credit intermediation |
| 524000 | Insurance carriers |
| 530000 | Real estate and rental and leasing |
| 540000 | Professional, scientific, and technical services |
| 540A00 | Professional and business services |
| 560000 | Administrative and support and waste management and remediation services |
| ... | 16 more codes |


### occupation_code

| Property | Value |
|----------|-------|
| filename | ci.occupation|
| size | 1.24 KB|
| #codes | 21|
| variables | occupation_code, occupation_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 000000 | All occupations |
| 000001 | All occupations, excluding sales |
| 111300 | Management, business, and financial occupations |
| 112900 | Management, professional and related occupations |
| 114300 | All white-collar occupations |
| 114301 | All white-collar occupations, excluding sales |
| 152900 | Professional and related occupations |
| 313900 | Service occupations |
| 410000 | Sales and related occupations |
| 414300 | Sales and office occupations |
| 430000 | Office and administrative support occupations |
| 43000D | Office and administrative support occupations (SOC 2010) |
| 454700 | Construction, and extraction, farming, fishing, and forestry occupations |
| 454900 | Natural resources, construction, and maintenance occupations |
| 455300 | All-blue collar occupations |
| 490000 | Installation, maintenance, and repair occupations |
| 510000 | Production occupations |
| 515300 | Production, transportation, and material moving occupations |
| 530000 | Transportation and material moving occupations |
| 53000D | Transportation and material moving occupations (SOC 2010) |
| ... | 1 more codes |


### subcell_code

| Property | Value |
|----------|-------|
| filename | ci.subcell|
| size | 0.49 KB|
| #codes | 15|
| variables | subcell_code, subcell_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 00 | All workers |
| 23 | Union |
| 24 | Nonunion |
| 27 | Excluding incentive-based pay |
| AA | Establishment Size |
| AB | Region and Division |
| AC | Metropolitan Statistical Areas |
| AD | Bargaining Status |
| AE | Work status |
| AF | Basis of pay |
| AG | Average Wage |
| AH | Civilian Wage Percentiles |
| AI | Private Wage Percentiles |
| AJ | Government Wage Percentiles |
| AK | Plan Sponsor |


### periodicity_code

| Property | Value |
|----------|-------|
| filename | ci.periodicity|
| size | 0.52 KB|
| #codes | 12|
| variables | periodicity_code, periodicity_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| A | 12-month percent change, current dollars |
| B | Current Dollar (Nominal) |
| C | Constant Dollar (Real) |
| D | Response Rates |
| I | Current dollar index number |
| P | Usable rate, updates |
| Q | 3-month percent change, current dollars |
| R | Usable rate, initiations |
| S | Survey response rate |
| T | Constant dollar index number |
| X | 3-month percent change, constant dollars |
| Z | 12-month percent change, constant dollars |


## Series Attributes

| Name | Type |
|------|------|
| area_code | `code`|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| seasonal | `other`|
| series_title | `text`|


### area_code (code)

| Property | Value |
|----------|-------|
| filename | ci.area|
| size | 1.50 KB|
| #codes | 33|
| variables | area_code, area_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 122 | Atlanta-Athens-Clarke County-Sandy Springs, GA-AL CSA |
| 148 | Boston-Worcester-Providence, MA-RI-NH CSA |
| 176 | Chicago-Naperville, IL-IN-WI CSA |
| 206 | Dallas-Fort Worth, TX-OK CSA |
| 220 | Detroit-Warren-Ann Arbor, MI CSA |
| 288 | Houston-Pasadena, TX CSA |
| 348 | Los Angeles-Long Beach, CA CSA |
| 378 | Minneapolis-St. Paul, MN-WI CSA |
| 408 | New York-Newark, NY-NJ-CT-PA CSA |
| 428 | Philadelphia-Reading-Camden, PA-NJ-DE-MD CSA |
| 488 | San Jose-San Francisco-Oakland, CA CSA |
| 500 | Seattle-Tacoma, WA CSA |
| 548 | Washington-Baltimore-Arlington, DC-MD-VA-WV-PA CSA |
| 33100 | Miami-Port St. Lucie-Fort Lauderdale, FL CSA |
| 38060 | Phoenix-Mesa, AZ CSA |
| 98100 | Northeast census region |
| 98200 | South census region |
| 98300 | Midwest census region |
| 98400 | West census region |
| 98999 | Regions, divisions, and statistical areas |
| ... | 13 more codes |


### begin_period (time)

| Value | Count |
|-------|-------|
| Q01 | 2352 |
| Q03 | 4 |
| Q04 | 114 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1982 | 1 |
| 2001 | 1850 |
| 2002 | 60 |
| 2003 | 122 |
| 2004 | 4 |
| 2005 | 18 |
| 2006 | 406 |
| 2008 | 1 |
| 2009 | 2 |
| 2010 | 2 |
| 2015 | 2 |
| 2016 | 2 |


### end_period (time)

| Value | Count |
|-------|-------|
| Q02 | 1968 |
| Q03 | 68 |
| Q04 | 434 |


### end_year (time)

| Value | Count |
|-------|-------|
| 2006 | 428 |
| 2008 | 24 |
| 2009 | 2 |
| 2022 | 44 |
| 2023 | 4 |
| 2025 | 1968 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | ci.footnote|
| size | 1.84 KB|
| #codes | 21|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| 2 | See Footnote 2 on <a href="/ncs/ect/cimapnote.htm#2" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| 3 | See Footnote 3 on <a href="/ncs/ect/cimapnote.htm#3" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| 8 | See Footnote 8 on <a href="/ncs/ect/cimapnote.htm#8" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| 9 | See Footnote 9 on <a href="/ncs/ect/cimapnote.htm#9" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| A | Dashes indicate data not available. |
| B | Includes wages, salaries, and employer costs for employee benefits. |
| C | See Footnote C on <a href="/ncs/ect/cimapnote.htm#C" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| D | See Footnote D on <a href="/ncs/ect/cimapnote.htm#D" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| E | See Footnote E on <a href="/ncs/ect/cimapnote.htm#E" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| F | See Footnote F on <a href="/ncs/ect/cimapnote.htm#F" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| G | Includes mining, construction, and manufacturing. |
| H | See Footnote H on <a href="/ncs/ect/cimapnote.htm#H" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| J | See Footnote J on <a href="/ncs/ect/cimapnote.htm#J" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| K | Includes ambulatory health services and social assistance, not shown separately. |
| N | Includes farming, fishing, and forestry occupations. |
| O | See Footnote O on <a href="/ncs/ect/cimapnote.htm#O" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| Q | The index for this series is not strictly comparable to other series in this family. |
| S | Historical data are available beginning with December 2005. |
| X | See Footnote X on <a href="/ncs/ect/cimapnote.htm#X" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| Y | See Footnote Y on <a href="/ncs/ect/cimapnote.htm#Y" target="new">www.bls.gov/ect/cimapnote.htm</a>. |
| ... | 1 more codes |


### seasonal (other)

No additional information available.



### series_title (text)

No additional information available.



