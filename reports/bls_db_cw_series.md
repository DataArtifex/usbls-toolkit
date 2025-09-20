# cw: Consumer Price Index - All Urban Wage earners and clerical workers

Report Date: 2025-09-19

## Series File

| Property | Value |
|----------|-------|
| filename | cw.series|
| size | 1.39 MB|
| #series | 7,867|
| #attributes | 13|
| variables | series_id, area_code, item_code, seasonal, periodicity_code, base_code, base_period, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the cw.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 7867 | 7867 | CWSR0000SA0 | 1 |
| area_code | 7867 | 58 | 0000 | 907 |
| item_code | 7867 | 318 | SA0 | 117 |
| seasonal | 7867 | 2 | U | 7594 |
| periodicity_code | 7867 | 2 | R | 4054 |
| base_code | 7867 | 2 | S | 7782 |
| base_period | 7867 | 27 | 1982-84=100 | 3788 |
| series_title | 7867 | 4088 | Admissions in U.S. city average, urban wage earners and clerical workers, not seasonally adjusted | 2 |
| footnote_codes | 0 | 0 | N/A | 0 |
| begin_year | 7867 | 62 | 1984 | 1646 |
| begin_period | 7867 | 15 | S01 | 3395 |
| end_year | 7867 | 9 | 2025 | 6228 |
| end_period | 7867 | 14 | S01 | 2977 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| periodicity_code | `A-Z` | `1` | `?P<periodicity_code>[A-Z]{1}` |
| area_code | `A-Z0-9` | `4` | `?P<area_code>[A-Z0-9]{4}` |
| item_code | `A-Z0-9` | `*` | `?P<item_code>[A-Z0-9]*` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | cw.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### periodicity_code

| Property | Value |
|----------|-------|
| filename | cw.periodicity|
| size | 0.06 KB|
| #codes | 2|
| variables | periodicity_code, periodicity_name|


#### Codes

| Value | Label |
|-------|-------|
| R | Monthly |
| S | Semi-Annual |


### area_code

| Property | Value |
|----------|-------|
| filename | cw.area|
| size | 2.13 KB|
| #codes | 58|
| variables | area_code, area_name, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 0000 | U.S. city average |
| 0100 | Northeast |
| 0110 | New England |
| 0120 | Middle Atlantic |
| 0200 | Midwest |
| 0230 | East North Central |
| 0240 | West North Central |
| 0300 | South |
| 0350 | South Atlantic |
| 0360 | East South Central |
| 0370 | West South Central |
| 0400 | West |
| 0480 | Mountain |
| 0490 | Pacific |
| A104 | Pittsburgh, PA |
| A210 | Cleveland-Akron, OH |
| A212 | Milwaukee-Racine, WI |
| A213 | Cincinnati-Hamilton, OH-KY-IN |
| A214 | Kansas City, MO-KS |
| A311 | Washington-Baltimore, DC-MD-VA-WV |
| ... | 38 more codes |


### item_code

| Property | Value |
|----------|-------|
| filename | cw.item|
| size | 12.71 KB|
| #codes | 318|
| variables | item_code, item_name, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| AA0 | All items - old base |
| AA0R | Purchasing power of the consumer dollar - old base |
| SA0 | All items |
| SA0E | Energy |
| SA0L1 | All items less food |
| SA0L1E | All items less food and energy |
| SA0L2 | All items less shelter |
| SA0L5 | All items less medical care |
| SA0LE | All items less energy |
| SA0R | Purchasing power of the consumer dollar |
| SA311 | Apparel less footwear |
| SAA | Apparel |
| SAA1 | Men's and boys' apparel |
| SAA2 | Women's and girls' apparel |
| SAC | Commodities |
| SACE | Energy commodities |
| SACL1 | Commodities less food |
| SACL11 | Commodities less food and beverages |
| SACL1E | Commodities less food and energy commodities |
| SAD | Durables |
| ... | 298 more codes |


## Series Attributes

| Name | Type |
|------|------|
| base_code | `code`|
| base_period | `time`|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| seasonal | `other`|
| series_title | `text`|


### base_code (code)

| Property | Value |
|----------|-------|
| filename | cw.base|
| size | 0.04 KB|
| #codes | 2|
| variables | base_code, base_name|


#### Codes

| Value | Label |
|-------|-------|
| A | Alternate |
| S | Current |


### base_period (time)

| Value | Count |
|-------|-------|
| 1967=100 | 53 |
| 1982-84=100 | 3788 |
| 1987=100 | 104 |
| APRIL 1978=100 | 20 |
| DECEMBER 1977=100 | 158 |
| DECEMBER 1982=100 | 3 |
| DECEMBER 1983=100 | 6 |
| DECEMBER 1984=100 | 178 |
| DECEMBER 1986=100 | 161 |
| DECEMBER 1988=100 | 3 |
| DECEMBER 1990=100 | 6 |
| DECEMBER 1993=100 | 79 |
| DECEMBER 1996=100 | 19 |
| DECEMBER 1997=100 | 1141 |
| DECEMBER 2001=100 | 115 |
| DECEMBER 2005=100 | 4 |
| DECEMBER 2007=100 | 3 |
| DECEMBER 2009=100 | 604 |
| DECEMBER 2017=100 | 1220 |
| FEBRUARY 1978=100 | 10 |
| JANUARY 1978=100 | 28 |
| MARCH 1978=100 | 20 |
| NOVEMBER 1977=100 | 42 |
| NOVEMBER 1984=100 | 72 |
| NOVEMBER 1996=100 | 24 |
| NOVEMBER 1997=100 | 4 |
| OCTOBER 1967=100 | 2 |


### begin_period (time)

| Value | Count |
|-------|-------|
| M01 | 875 |
| M02 | 41 |
| M03 | 59 |
| M04 | 12 |
| M05 | 44 |
| M06 | 14 |
| M08 | 38 |
| M09 | 1 |
| M10 | 10 |
| M11 | 325 |
| M12 | 2616 |
| M13 | 19 |
| S01 | 3395 |
| S02 | 375 |
| S03 | 43 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1913 | 8 |
| 1914 | 53 |
| 1917 | 24 |
| 1935 | 72 |
| 1939 | 5 |
| 1943 | 1 |
| 1946 | 3 |
| 1947 | 92 |
| 1950 | 1 |
| 1952 | 84 |
| 1953 | 27 |
| 1956 | 7 |
| 1957 | 16 |
| 1960 | 2 |
| 1963 | 29 |
| 1964 | 2 |
| 1965 | 13 |
| 1966 | 125 |
| 1967 | 115 |
| 1969 | 4 |
| 1971 | 63 |
| 1972 | 2 |
| 1975 | 97 |
| 1976 | 176 |
| 1977 | 575 |
| 1978 | 104 |
| 1980 | 3 |
| 1981 | 40 |
| 1982 | 38 |
| 1983 | 4 |
| 1984 | 1646 |
| 1985 | 178 |
| 1986 | 69 |
| 1987 | 99 |
| 1988 | 2 |
| 1989 | 15 |
| 1990 | 7 |
| 1991 | 6 |
| 1992 | 5 |
| 1993 | 49 |
| 1994 | 41 |
| 1995 | 2 |
| 1996 | 23 |
| 1997 | 474 |
| 1998 | 430 |
| 1999 | 9 |
| 2000 | 3 |
| 2001 | 3 |
| 2002 | 47 |
| 2003 | 7 |
| 2004 | 3 |
| 2005 | 5 |
| 2006 | 5 |
| 2007 | 2 |
| 2008 | 1 |
| 2009 | 199 |
| 2010 | 343 |
| 2014 | 1 |
| 2015 | 64 |
| 2017 | 1497 |
| 2018 | 845 |
| 2019 | 2 |


### end_period (time)

| Value | Count |
|-------|-------|
| M01 | 1 |
| M02 | 3 |
| M03 | 10 |
| M04 | 5 |
| M05 | 6 |
| M06 | 5 |
| M07 | 343 |
| M08 | 2886 |
| M11 | 1 |
| M12 | 11 |
| M13 | 783 |
| S01 | 2977 |
| S02 | 1 |
| S03 | 835 |


### end_year (time)

| Value | Count |
|-------|-------|
| 1986 | 168 |
| 1997 | 53 |
| 2017 | 899 |
| 2018 | 4 |
| 2019 | 2 |
| 2021 | 90 |
| 2023 | 11 |
| 2024 | 412 |
| 2025 | 6228 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | cw.footnote|
| size | 0.03 KB|
| #codes | 0|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|


### seasonal (other)

No additional information available.



### series_title (text)

No additional information available.



