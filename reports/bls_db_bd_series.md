# bd: Business Employment Dynamics

Report Date: 2025-11-05

## Series File

| Property | Value |
|----------|-------|
| filename | bd.series|
| size | 5.35 MB|
| #series | 34,464|
| #attributes | 19|
| variables | series_id, seasonal, msa_code, state_code, county_code, industry_code, unitanalysis_code, dataelement_code, sizeclass_code, dataclass_code, ratelevel_code, periodicity_code, ownership_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the bd.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 34464 | 34464 | BDS0000000000000000110001LQ5 | 1 |
| seasonal | 34464 | 2 | U | 18060 |
| msa_code | 34464 | 1 | 00000 | 34464 |
| state_code | 34464 | 54 | 00 | 5752 |
| county_code | 34464 | 1 | 000 | 34464 |
| industry_code | 34464 | 91 | 000000 | 5496 |
| unitanalysis_code | 34464 | 1 | 1 | 34464 |
| dataelement_code | 34464 | 2 | 1 | 17340 |
| sizeclass_code | 34464 | 32 | 00 | 33720 |
| dataclass_code | 34464 | 8 | 01 | 5560 |
| ratelevel_code | 34464 | 2 | L | 17496 |
| periodicity_code | 34464 | 2 | Q | 32808 |
| ownership_code | 34464 | 1 | 5 | 34464 |
| series_title | 34464 | 916 | Gross job gains | 1312 |
| footnote_codes | 4840 | 1 | 1 | 4840 |
| begin_year | 34464 | 3 | 1992 | 32504 |
| begin_period | 34464 | 2 | Q03 | 32504 |
| end_year | 34464 | 1 | 2024 | 34464 |
| end_period | 34464 | 1 | Q04 | 34464 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| msa_code | `\d` | `5` | `?P<msa_code>[\d]{5}` |
| state_code | `\d` | `2` | `?P<state_code>[\d]{2}` |
| county_code | `\d` | `3` | `?P<county_code>[\d]{3}` |
| industry_code | `\d` | `6` | `?P<industry_code>[\d]{6}` |
| unitanalysis_code | `\d` | `1` | `?P<unitanalysis_code>[\d]{1}` |
| dataelement_code | `\d` | `1` | `?P<dataelement_code>[\d]{1}` |
| sizeclass_code | `\d` | `2` | `?P<sizeclass_code>[\d]{2}` |
| dataclass_code | `\d` | `2` | `?P<dataclass_code>[\d]{2}` |
| ratelevel_code | `A-Z` | `1` | `?P<ratelevel_code>[A-Z]{1}` |
| periodicity_code | `A-Z` | `1` | `?P<periodicity_code>[A-Z]{1}` |
| ownership_code | `\d` | `1` | `?P<ownership_code>[\d]{1}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | bd.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally adjusted |
| U | Not seasonally adjusted |


### msa_code

| Property | Value |
|----------|-------|
| filename | bd.msa|
| size | 0.03 KB|
| #codes | 1|
| variables | msa_code, msa_name|


#### Codes

| Value | Label |
|-------|-------|
| 0 | National |


### state_code

| Property | Value |
|----------|-------|
| filename | bd.state|
| size | 0.75 KB|
| #codes | 54|
| variables | state_code, state_name|


#### Codes

| Value | Label |
|-------|-------|
| 0 | U.S. totals |
| 1 | Alabama |
| 2 | Alaska |
| 4 | Arizona |
| 5 | Arkansas |
| 6 | California |
| 8 | Colorado |
| 9 | Connecticut |
| 10 | Delaware |
| 11 | District of Columbia |
| 12 | Florida |
| 13 | Georgia |
| 15 | Hawaii |
| 16 | Idaho |
| 17 | Illinois |
| 18 | Indiana |
| 19 | Iowa |
| 20 | Kansas |
| 21 | Kentucky |
| 22 | Louisiana |
| ... | 34 more codes |


### county_code

| Property | Value |
|----------|-------|
| filename | bd.county|
| size | 0.04 KB|
| #codes | 1|
| variables | county_code, county_name|


#### Codes

| Value | Label |
|-------|-------|
| 0 | National |


### industry_code

| Property | Value |
|----------|-------|
| filename | bd.industry|
| size | 4.35 KB|
| #codes | 91|
| variables | industry_code, industry_name, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 0 | Total private |
| 100000 | Goods-producing |
| 100010 | Natural resources and mining |
| 100020 | Construction |
| 100030 | Manufacturing |
| 200000 | Service-providing |
| 200010 | Wholesale trade |
| 200020 | Retail trade |
| 200030 | Transportation and warehousing |
| 200040 | Utilities |
| 200050 | Information |
| 200060 | Financial activities |
| 200070 | Professional and business services |
| 200080 | Education and health services |
| 200090 | Leisure and hospitality |
| 200100 | Other services (except public administration) |
| 300111 | Crop production |
| 300112 | Animal production and aquaculture |
| 300113 | Forestry and logging |
| 300114 | Hunting, fishing, and trapping |
| ... | 71 more codes |


### unitanalysis_code

| Property | Value |
|----------|-------|
| filename | bd.unitanalysis|
| size | 0.05 KB|
| #codes | 1|
| variables | unitanalysis_code, unitanalysis_name|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Establishment |


### dataelement_code

| Property | Value |
|----------|-------|
| filename | bd.dataelement|
| size | 0.08 KB|
| #codes | 2|
| variables | dataelement_code, dataelement_name|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Employment |
| 2 | Number of Establishments |


### sizeclass_code

| Property | Value |
|----------|-------|
| filename | bd.sizeclass|
| size | 0.56 KB|
| #codes | 32|
| variables | sizeclass_code, sizeclass_name|


#### Codes

| Value | Label |
|-------|-------|
| 0 | All size classes |
| 1 | 1 to 4 employees |
| 2 | 5 to 9 employees |
| 3 | 10 to 19 employees |
| 4 | 20 to 49 employees |
| 5 | 50 to 99 employees |
| 6 | 100 to 249 employees |
| 7 | 250 to 499 employees |
| 8 | 500 to 999 employees |
| 9 | 1,000 or more employees |
| 10 | 1 job |
| 11 | 2 jobs |
| 12 | 3 jobs |
| 13 | 4 jobs |
| 14 | 5 jobs |
| 15 | 6 jobs |
| 16 | 7 jobs |
| 17 | 8 jobs |
| 18 | 9 jobs |
| 19 | 10 jobs |
| ... | 12 more codes |


### dataclass_code

| Property | Value |
|----------|-------|
| filename | bd.dataclass|
| size | 0.26 KB|
| #codes | 8|
| variables | dataclass_code, dataclass_name, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Gross Job Gains |
| 2 | Expansions |
| 3 | Openings |
| 4 | Gross Job Losses |
| 5 | Contractions |
| 6 | Closings |
| 7 | Establishment Births |
| 8 | Establishment Deaths |


### ratelevel_code

| Property | Value |
|----------|-------|
| filename | bd.ratelevel|
| size | 0.05 KB|
| #codes | 2|
| variables | ratelevel_code, ratelevel_name|


#### Codes

| Value | Label |
|-------|-------|
| L | Level |
| R | Rate |


### periodicity_code

| Property | Value |
|----------|-------|
| filename | bd.periodicity|
| size | 0.06 KB|
| #codes | 2|
| variables | periodicity_code, periodicity_name|


#### Codes

| Value | Label |
|-------|-------|
| A | Annual |
| Q | Quarterly |


### ownership_code

| Property | Value |
|----------|-------|
| filename | bd.ownership|
| size | 0.05 KB|
| #codes | 1|
| variables | ownership_code, ownership_name|


#### Codes

| Value | Label |
|-------|-------|
| 5 | Private Sector |


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
| Q01 | 1960 |
| Q03 | 32504 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1992 | 32504 |
| 1994 | 1632 |
| 2000 | 328 |


### end_period (time)

| Value | Count |
|-------|-------|
| Q04 | 34464 |


### end_year (time)

| Value | Count |
|-------|-------|
| 2024 | 34464 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | bd.footnote|
| size | 0.15 KB|
| #codes | 2|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Total private includes unclassified sector, not shown separately |
| 2 | An administrative event occurred during this quarter |


### seasonal (time)

| Value | Count |
|-------|-------|
| S | 16404 |
| U | 18060 |


### series_title (text)

No additional information available.



