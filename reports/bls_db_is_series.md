# is: Occupational Injuries and Illnesses Industry Data)

Report Date: 2025-11-05

## Series File

| Property | Value |
|----------|-------|
| filename | is.series|
| size | 119.39 MB|
| #series | 887,896|
| #attributes | 13|
| variables | series_id, seasonal, supersector_code, industry_code, data_type_code, case_type_code, area_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the is.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 887896 | 887896 | ISU00000000000000 | 1 |
| seasonal | 887896 | 1 | U | 887896 |
| supersector_code | 887896 | 14 | MFG | 197812 |
| industry_code | 887896 | 1304 | 000000 | 61228 |
| data_type_code | 887896 | 36 | 0 | 122950 |
| case_type_code | 887896 | 20 | 0 | 112571 |
| area_code | 887896 | 236 | 100 | 178680 |
| series_title | 887896 | 1 | Industry-level data from the Survey of Occupational Injuries and Illnesses (SOII) | 887896 |
| footnote_codes | 0 | 0 | N/A | 0 |
| begin_year | 887896 | 10 | 2014 | 636368 |
| begin_period | 887896 | 1 | A01 | 887896 |
| end_year | 887896 | 10 | 2023 | 388460 |
| end_period | 887896 | 1 | A01 | 887896 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| supersector_code | `\d` | `3` | `?P<supersector_code>[\d]{3}` |
| industry_code | `\d` | `6` | `?P<industry_code>[\d]{6}` |
| data_type_code | `\d` | `3` | `?P<data_type_code>[\d]{3}` |
| case_type_code | `\d` | `1` | `?P<case_type_code>[\d]{1}` |
| area_code | `\d` | `6` | `?P<area_code>[\d]{6}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | is.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### supersector_code

| Property | Value |
|----------|-------|
| filename | is.supersector|
| size | 0.51 KB|
| #codes | 14|
| variables | supersector_code, supersector_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 000 | All |
| CON | Construction |
| EHS | Education and health services |
| FIA | Financial activities |
| GP1 | Goods producing |
| INF | Information |
| LEH | Leisure and hospitality |
| MFG | Manufacturing |
| NRM | Natural resources and mining |
| OTS | Other services |
| PAD | Public administration |
| PBS | Professional and business services |
| SP1 | Service providing |
| TTU | Trade, transportation, and utilities |


### industry_code

| Property | Value |
|----------|-------|
| filename | is.industry|
| size | 74.95 KB|
| #codes | 1,304|
| variables | supersector_code, industry_code, industry_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 000000 | All workers |
| 236000 | Construction of buildings |
| 236100 | Residential building construction |
| 236110 | Residential building construction |
| 236115 | New single-family housing construction (except for-sale builders) |
| 236116 | New multifamily housing construction (except for-sale builders) |
| 236117 | New housing for-sale builders |
| 236118 | Residential remodelers |
| 236200 | Nonresidential building construction |
| 236210 | Industrial building construction |
| 236220 | Commercial and institutional building construction |
| 237000 | Heavy and civil engineering construction |
| 237100 | Utility system construction |
| 237110 | Water and sewer line and related structures construction |
| 237120 | Oil and gas pipeline and related structures construction |
| 237130 | Power and communication line and related structures construction |
| 237200 | Land subdivision |
| 237300 | Highway, street, and bridge construction |
| 237900 | Other heavy and civil engineering construction |
| 238000 | Specialty trade contractors |
| ... | 1284 more codes |


### data_type_code

Codes file/list not available.

### case_type_code

Codes file/list not available.

### area_code

| Property | Value |
|----------|-------|
| filename | is.area|
| size | 10.06 KB|
| #codes | 236|
| variables | area_code, area_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 0 | All ownerships, All U.S. |
| 1 | All ownerships, Alabama |
| 2 | All ownerships, Alaska |
| 4 | All ownerships, Arizona |
| 5 | All ownerships, Arkansas |
| 6 | All ownerships, California |
| 8 | All ownerships, Colorado |
| 9 | All ownerships, Connecticut |
| 10 | All ownerships, Delaware |
| 11 | All ownerships, District of Columbia |
| 13 | All ownerships, Georgia |
| 15 | All ownerships, Hawaii |
| 17 | All ownerships, Illinois |
| 18 | All ownerships, Indiana |
| 19 | All ownerships, Iowa |
| 20 | All ownerships, Kansas |
| 21 | All ownerships, Kentucky |
| 22 | All ownerships, Louisiana |
| 23 | All ownerships, Maine |
| 24 | All ownerships, Maryland |
| ... | 216 more codes |


## Series Attributes

| Name | Type |
|------|------|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| seasonal | `time`|
| series_title | `text`|


### begin_period (time)

| Value | Count |
|-------|-------|
| A01 | 887896 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 2014 | 636368 |
| 2015 | 103432 |
| 2016 | 43448 |
| 2017 | 26442 |
| 2018 | 18234 |
| 2019 | 27532 |
| 2020 | 11372 |
| 2021 | 9052 |
| 2022 | 7348 |
| 2023 | 4668 |


### end_period (time)

| Value | Count |
|-------|-------|
| A01 | 887896 |


### end_year (time)

| Value | Count |
|-------|-------|
| 2014 | 20934 |
| 2015 | 22318 |
| 2016 | 32082 |
| 2017 | 33302 |
| 2018 | 67850 |
| 2019 | 186062 |
| 2020 | 27452 |
| 2021 | 39026 |
| 2022 | 70410 |
| 2023 | 388460 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | is.footnote|
| size | 0.12 KB|
| #codes | 4|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| A | Industry added in 2019 |
| C | Less than 15 cases |
| L | Less than 50 cases |
| Z | Rate rounded to zero |


### seasonal (time)

| Value | Count |
|-------|-------|
| U | 887896 |


### series_title (text)

No additional information available.



