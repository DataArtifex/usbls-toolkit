# la: Local Area Unemployment Statistics

Report Date: 2025-09-19

## Series File

| Property | Value |
|----------|-------|
| filename | la.series|
| size | 3.89 MB|
| #series | 33,881|
| #attributes | 12|
| variables | series_id, area_type_code, area_code, measure_code, seasonal, srd_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the la.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 33881 | 33881 | LASBS060000000000003 | 1 |
| area_type_code | 33881 | 14 | F | 12900 |
| area_code | 33881 | 8325 | CT3651000000000 | 13 |
| measure_code | 33881 | 7 | 03 | 8404 |
| seasonal | 33881 | 2 | U | 33459 |
| srd_code | 33881 | 53 | 48 | 2277 |
| series_title | 33881 | 33673 | Employment: Alexandria city, VA (U) | 2 |
| footnote_codes | 12 | 1 | A | 12 |
| begin_year | 33881 | 26 | 1990 | 30048 |
| begin_period | 33881 | 1 | M01 | 33881 |
| end_year | 33881 | 5 | 2025 | 33725 |
| end_period | 33881 | 2 | M07 | 33725 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| area_code | `A-Z0-9` | `15` | `?P<area_code>[A-Z0-9]{15}` |
| measure_code | `0-9` | `2` | `?P<measure_code>[0-9]{2}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | la.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### area_code

| Property | Value |
|----------|-------|
| filename | la.area|
| size | 428.01 KB|
| #codes | 8,325|
| variables | area_type_code, area_code, area_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| ST0100000000000 | Alabama |
| ST0200000000000 | Alaska |
| ST0400000000000 | Arizona |
| ST0500000000000 | Arkansas |
| ST0600000000000 | California |
| ST0800000000000 | Colorado |
| ST0900000000000 | Connecticut |
| ST1000000000000 | Delaware |
| ST1100000000000 | District of Columbia |
| ST1200000000000 | Florida |
| ST1300000000000 | Georgia |
| ST1500000000000 | Hawaii |
| ST1600000000000 | Idaho |
| ST1700000000000 | Illinois |
| ST1800000000000 | Indiana |
| ST1900000000000 | Iowa |
| ST2000000000000 | Kansas |
| ST2100000000000 | Kentucky |
| ST2200000000000 | Louisiana |
| ST2300000000000 | Maine |
| ... | 8305 more codes |


### measure_code

| Property | Value |
|----------|-------|
| filename | la.measure|
| size | 0.20 KB|
| #codes | 7|
| variables | measure_code, measure_text|


#### Codes

| Value | Label |
|-------|-------|
| 3 | unemployment rate |
| 4 | unemployment |
| 5 | employment |
| 6 | labor force |
| 7 | employment-population ratio |
| 8 | labor force participation rate |
| 9 | civilian noninstitutional population |


## Series Attributes

| Name | Type |
|------|------|
| area_type_code | `code`|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| seasonal | `other`|
| series_title | `text`|
| srd_code | `code`|


### area_type_code (code)

| Property | Value |
|----------|-------|
| filename | la.area_type|
| size | 0.44 KB|
| #codes | 14|
| variables | area_type_code, area_type_text|


#### Codes

| Value | Label |
|-------|-------|
| A | Statewide |
| B | Metropolitan areas |
| C | Metropolitan divisions |
| D | Micropolitan areas |
| E | Combined areas |
| F | Counties and equivalents |
| G | Cities and towns above 25,000 population |
| H | Cities and towns below 25,000 population in New England |
| I | Parts of cities that cross county boundaries |
| J | Multi-entity small labor market areas |
| K | Intrastate parts of interstate areas |
| L | Balance of state areas |
| M | Census regions |
| N | Census divisions |


### begin_period (time)

| Value | Count |
|-------|-------|
| M01 | 33881 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1976 | 817 |
| 1990 | 30048 |
| 1991 | 12 |
| 1992 | 16 |
| 1993 | 8 |
| 1994 | 56 |
| 1995 | 120 |
| 1996 | 4 |
| 1997 | 144 |
| 1998 | 120 |
| 1999 | 152 |
| 2000 | 1068 |
| 2008 | 20 |
| 2010 | 728 |
| 2011 | 4 |
| 2012 | 16 |
| 2013 | 40 |
| 2015 | 24 |
| 2016 | 40 |
| 2017 | 28 |
| 2018 | 28 |
| 2019 | 40 |
| 2020 | 264 |
| 2021 | 20 |
| 2022 | 20 |
| 2023 | 44 |


### end_period (time)

| Value | Count |
|-------|-------|
| M07 | 33725 |
| M13 | 156 |


### end_year (time)

| Value | Count |
|-------|-------|
| 1999 | 20 |
| 2009 | 40 |
| 2015 | 60 |
| 2019 | 36 |
| 2025 | 33725 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | la.footnote|
| size | 0.48 KB|
| #codes | 7|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| A | Area boundaries do not reflect official OMB definitions. |
| N | Not available. |
| P | Preliminary. |
| U | The annual average cannot be calculated due to missing monthly data. |
| V | The survey was not conducted due to bad weather. Interpolated data were seasonally adjusted. |
| W | The household survey was not conducted for this month due to bad weather. Data were interpolated. |
| Y | Data reflect controlling to interpolated statewide totals because the survey was not conducted. |


### seasonal (other)

No additional information available.



### series_title (text)

No additional information available.



### srd_code (code)

Codes file/list not available.

