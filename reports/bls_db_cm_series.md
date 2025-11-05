# cm: Employer Costs for Employee Compensation (NAICS)

Report Date: 2025-11-05

## Series File

| Property | Value |
|----------|-------|
| filename | cm.series|
| size | 1.49 MB|
| #series | 7,998|
| #attributes | 15|
| variables | series_id, seasonal, owner_code, industry_code, occupation_code, subcell_code, area_code, datatype_code, estimate_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the cm.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 7998 | 7998 | CMU1010000000000D | 1 |
| seasonal | 7998 | 1 | U | 7998 |
| owner_code | 7998 | 3 | 2 | 6642 |
| industry_code | 7998 | 32 | 000000 | 3312 |
| occupation_code | 7998 | 18 | 000000 | 4842 |
| subcell_code | 7998 | 11 | 00 | 5360 |
| area_code | 7998 | 31 | 99999 | 7068 |
| datatype_code | 7998 | 8 | D | 3918 |
| estimate_code | 7998 | 28 | 01 | 720 |
| series_title | 7998 | 7998 | All Civilian Insurance plans for Construction and extraction occupations; Cost per hour worked | 1 |
| footnote_codes | 1920 | 45 | E | 326 |
| begin_year | 7998 | 3 | 2004 | 5218 |
| begin_period | 7998 | 2 | Q01 | 5470 |
| end_year | 7998 | 3 | 2025 | 7486 |
| end_period | 7998 | 3 | Q02 | 7234 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| owner_code | `\d` | `1` | `?P<owner_code>[\d]{1}` |
| industry_code | `\d` | `4` | `?P<industry_code>[\d]{4}` |
| occupation_code | `\d` | `3` | `?P<occupation_code>[\d]{3}` |
| subcell_code | `\d` | `2` | `?P<subcell_code>[\d]{2}` |
| datatype_code | `A-Z` | `1` | `?P<datatype_code>[A-Z]{1}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | cm.seasonal|
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
| filename | cm.owner|
| size | 0.16 KB|
| #codes | 3|
| variables | owner_code, owner_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Civilian workers |
| 2 | Private industry workers |
| 3 | State and local government workers |


### industry_code

| Property | Value |
|----------|-------|
| filename | cm.industry|
| size | 1.47 KB|
| #codes | 33|
| variables | industry_code, industry_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 000000 | All workers |
| 220000 | Utilities |
| 230000 | Construction |
| 300000 | Manufacturing |
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
| 600000 | Education and health services |
| 610000 | Educational services |
| ... | 13 more codes |


### occupation_code

| Property | Value |
|----------|-------|
| filename | cm.occupation|
| size | 1.08 KB|
| #codes | 19|
| variables | occupation_code, occupation_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 000000 | All workers |
| 111300 | Management, business, and financial occupations |
| 112900 | Management, professional and related occupations |
| 152900 | Professional and related occupations |
| 250001 | Teachers |
| 252000 | Primary, secondary, and special education school teachers |
| 291111 | Registered nurses |
| 313900 | Service occupations |
| 410000 | Sales and related occupations |
| 414300 | Sales and office occupations |
| 430000 | Office and administrative support occupations |
| 454700 | Construction, and extraction, farming, fishing, and forestry occupations |
| 454900 | Natural resources, construction, and maintenance occupations |
| 470000 | Construction and extraction occupations |
| 490000 | Installation, maintenance, and repair occupations |
| 510000 | Production occupations |
| 515300 | Production, transportation, and material moving occupations |
| 530000 | Transportation and material moving occupations |
| DISCON | Discontinued Codes |


### subcell_code

| Property | Value |
|----------|-------|
| filename | cm.subcell|
| size | 0.70 KB|
| #codes | 22|
| variables | subcell_code, subcell_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 00 | All workers |
| 01 | Less than 100 workers |
| 02 | Less than 50 workers |
| 04 | 50-99 workers |
| 05 | 100 workers or more |
| 06 | 100-499 workers |
| 07 | 500 workers or more |
| 23 | Union |
| 24 | Nonunion |
| 25 | Full time |
| 26 | Part time |
| AA | Establishment Size |
| AB | Region and Division |
| AC | Metropolitan Statistical Areas |
| AD | Bargaining Status |
| AE | Full-time and Part-time Work Status |
| AF | Time and Incentive Status |
| AG | Average Wage |
| AH | Civilian Wage Percentiles |
| AI | Private Wage Percentiles |
| ... | 2 more codes |


### datatype_code

| Property | Value |
|----------|-------|
| filename | cm.datatype|
| size | 0.71 KB|
| #codes | 8|
| variables | datatype_code, datatype_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| D | Cost of compensation (Cost per hour worked) |
| L | Average employer cost per employee hour worked at 50th percentile (median), constant dollar |
| M | Average employer cost per employee worked at 50th percentile (median), current dollar |
| N | Average employer cost per employee hour worked at 90th percentile, current dollar |
| P | Percent of total compensation |
| R | Average employer cost per employee hour worked at 90th percentile, constant dollar |
| T | Average employer cost per employee hour worked at 10th percentile, current dollar |
| X | Average employer cost per employee hour worked at 10th percentile, constant dollar |


## Series Attributes

| Name | Type |
|------|------|
| area_code | `code`|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| estimate_code | `code`|
| footnote_codes | `code`|
| seasonal | `time`|
| series_title | `text`|


### area_code (code)

| Property | Value |
|----------|-------|
| filename | cm.area|
| size | 1.52 KB|
| #codes | 33|
| variables | area_code, area_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 122 | Atlanta-Athens-Clarke County-Sandy Springs, GA CSA |
| 148 | Boston-Worcester-Providence, MA-RI-NH-CT CSA |
| 176 | Chicago-Naperville, IL-IN-WI CSA |
| 206 | Dallas-Fort Worth, TX-OK CSA |
| 220 | Detroit-Warren-Ann Arbor, MI CSA |
| 288 | Houston-The Woodlands, TX CSA |
| 348 | Los Angeles-Long Beach, CA CSA |
| 378 | Minneapolis-St. Paul, MN-WI CSA |
| 408 | New York-Newark, NY-NJ-CT-PA CSA |
| 428 | Philadelphia-Reading-Camden, PA-NJ-DE-MD CSA |
| 488 | San Jose-San Francisco-Oakland, CA CSA |
| 500 | Seattle-Tacoma, WA CSA |
| 548 | Washington-Baltimore-Arlington, DC-MD-VA-WV-PA CSA |
| 33100 | Miami-Fort Lauderdale-Port St. Lucie, FL CSA |
| 38060 | Phoenix-Mesa-Scottsdale, AZ MSA |
| 98100 | Northeast census region |
| 98200 | South census region |
| 98300 | Midwest census region |
| 98400 | West census region |
| 98999 | Regions, divisions, and statistical areas |
| ... | 13 more codes |


### begin_period (time)

| Value | Count |
|-------|-------|
| Q01 | 5470 |
| Q04 | 2528 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 2004 | 5218 |
| 2006 | 2528 |
| 2009 | 252 |


### end_period (time)

| Value | Count |
|-------|-------|
| Q01 | 252 |
| Q02 | 7234 |
| Q03 | 512 |


### end_year (time)

| Value | Count |
|-------|-------|
| 2006 | 404 |
| 2008 | 108 |
| 2025 | 7486 |


### estimate_code (code)

| Property | Value |
|----------|-------|
| filename | cm.estimate|
| size | 0.88 KB|
| #codes | 28|
| variables | estimate_code, estimate_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Total compensation |
| 2 | Wages and salaries |
| 3 | Total benefits |
| 4 | Paid leave |
| 5 | Vacation |
| 6 | Holiday |
| 7 | Sick leave |
| 8 | Personal leave |
| 9 | Supplemental pay |
| 10 | Overtime and premium pay |
| 11 | Shift differentials |
| 12 | Nonproduction bonuses |
| 13 | Insurance |
| 14 | Life insurance |
| 15 | Health insurance |
| 16 | Short-term disability insurance |
| 17 | Long-term disability insurance |
| 18 | Retirement and savings |
| 19 | Defined benefit |
| 20 | Defined contribution |
| ... | 8 more codes |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | cm.footnote|
| size | 2.79 KB|
| #codes | 27|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| 2 | Registered Nurses estimates from December 2013 forward are based on the 2010 Standard Occupational Classification. For more information on classification changes, please see www.bls.gov/soc. |
| 3 | Estimates from December 2013 to March 2014 for this series were corrected, details are available at www.bls.gov/bls/ecec_correction_091014.htm |
| 4 | The relative standard error for this estimate is equal to or greater than 30 percent. |
| 5 | The relative standard error is not available for percent of total compensation estimates. |
| 6 | The relative standard error for this estimate is not currently available. |
| 8 | The relative standard error is not available as the cost per hour worked is $0.01 or less. |
| A | Cost per hour worked is $0.01 or less. |
| B | Less than .05 percent. |
| C | See <a href="http://www.bls.gov/ncs/ect/mapnote.htm#C" target="new">www.bls.gov/ncs/ect/mapnote.htm</a> for the definition of civilian workers. |
| D | See <a href="http://www.bls.gov/ncs/ect/mapnote.htm#D" target="new">www.bls.gov/ncs/ect/mapnote.htm</a> for the definition of the goods-producing sector. |
| E | See <a href="http://www.bls.gov/ncs/ect/mapnote.htm#E" target="new">www.bls.gov/ncs/ect/mapnote.htm</a> for the definition of the service-providing sector. |
| F | Includes premium pay for work in addition to the regular work schedule (for example, overtime). |
| G | Comprises the Old-Age, Survivors, and Disability Insurance (OASDI) program. |
| H | Includes severance pay and supplemental unemployment benefits. |
| I | The states that compose the New England census division are: CT, ME, MA, NH, RI, and VT. |
| J | The states that compose the Middle Atlantic census division are: NJ, NY, and PA. |
| K | The states that compose the South Atlantic census division are: DE, DC, FL, GA, MD, NC, SC, VA, and WV. |
| L | The states that compose the East South Central census division are: AL, KY, MS, and TN. |
| M | The states that compose the West South Central census division are: AR, LA, OK, and TX. |
| N | The states that compose the East North Central census division are: IL, IN, MI, OH, and WI. |
| ... | 7 more codes |


### seasonal (time)

| Value | Count |
|-------|-------|
| U | 7998 |


### series_title (text)

No additional information available.



