# cu: Consumer Price Index - All Urban Consumers

Report Date: 2025-09-19

## Series File

| Property | Value |
|----------|-------|
| filename | cu.series|
| size | 1.28 MB|
| #series | 8,103|
| #attributes | 13|
| variables | series_id, area_code, item_code, seasonal, periodicity_code, base_code, base_period, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the cu.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 8103 | 8103 | CUSR0000SA0 | 1 |
| area_code | 8103 | 58 | 0000 | 1115 |
| item_code | 8103 | 400 | SA0 | 117 |
| seasonal | 8103 | 2 | U | 7778 |
| periodicity_code | 8103 | 2 | R | 4202 |
| base_code | 8103 | 2 | S | 8018 |
| base_period | 8103 | 27 | 1982-84=100 | 3893 |
| series_title | 8103 | 4236 | Admission to movies, theaters, and concerts in U.S. city average, all urban consumers, not seasonally adjusted | 2 |
| footnote_codes | 0 | 0 | N/A | 0 |
| begin_year | 8103 | 65 | 1984 | 1707 |
| begin_period | 8103 | 16 | S01 | 3481 |
| end_year | 8103 | 15 | 2025 | 6429 |
| end_period | 8103 | 15 | S01 | 3059 |


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
| filename | cu.seasonal|
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
| filename | cu.periodicity|
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
| filename | cu.area|
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
| filename | cu.item|
| size | 16.19 KB|
| #codes | 400|
| variables | item_code, item_name, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| AA0 | All items - old base |
| AA0R | Purchasing power of the consumer dollar - old base |
| SA0 | All items |
| SA0E | Energy |
| SA0L1 | All items less food |
| SA0L12 | All items less food and shelter |
| SA0L12E | All items less food, shelter, and energy |
| SA0L12E4 | All items less food, shelter, energy, and used cars and trucks |
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
| ... | 380 more codes |


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
| filename | cu.base|
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
| 1982-84=100 | 3893 |
| 1987=100 | 104 |
| APRIL 1978=100 | 20 |
| DECEMBER 1977=100 | 158 |
| DECEMBER 1982=100 | 181 |
| DECEMBER 1983=100 | 9 |
| DECEMBER 1986=100 | 165 |
| DECEMBER 1988=100 | 3 |
| DECEMBER 1990=100 | 6 |
| DECEMBER 1993=100 | 79 |
| DECEMBER 1996=100 | 19 |
| DECEMBER 1997=100 | 1245 |
| DECEMBER 2001=100 | 117 |
| DECEMBER 2005=100 | 11 |
| DECEMBER 2007=100 | 10 |
| DECEMBER 2009=100 | 606 |
| DECEMBER 2017=100 | 1220 |
| DECEMBER 2019=100 | 2 |
| FEBRUARY 1978=100 | 10 |
| JANUARY 1978=100 | 28 |
| MARCH 1978=100 | 20 |
| NOVEMBER 1977=100 | 42 |
| NOVEMBER 1982=100 | 72 |
| NOVEMBER 1996=100 | 24 |
| NOVEMBER 1997=100 | 4 |
| OCTOBER 1967=100 | 2 |


### begin_period (time)

| Value | Count |
|-------|-------|
| M01 | 884 |
| M02 | 39 |
| M03 | 61 |
| M04 | 12 |
| M05 | 44 |
| M06 | 14 |
| M07 | 1 |
| M08 | 38 |
| M09 | 1 |
| M10 | 10 |
| M11 | 357 |
| M12 | 2720 |
| M13 | 21 |
| S01 | 3481 |
| S02 | 377 |
| S03 | 43 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1913 | 8 |
| 1914 | 53 |
| 1917 | 24 |
| 1935 | 74 |
| 1939 | 12 |
| 1943 | 1 |
| 1946 | 3 |
| 1947 | 96 |
| 1950 | 1 |
| 1951 | 1 |
| 1952 | 85 |
| 1953 | 28 |
| 1956 | 7 |
| 1957 | 16 |
| 1960 | 2 |
| 1961 | 1 |
| 1963 | 29 |
| 1964 | 2 |
| 1965 | 13 |
| 1966 | 125 |
| 1967 | 123 |
| 1969 | 4 |
| 1971 | 63 |
| 1972 | 2 |
| 1975 | 97 |
| 1976 | 176 |
| 1977 | 600 |
| 1978 | 108 |
| 1980 | 3 |
| 1981 | 40 |
| 1982 | 157 |
| 1983 | 7 |
| 1984 | 1707 |
| 1985 | 3 |
| 1986 | 71 |
| 1987 | 100 |
| 1988 | 2 |
| 1989 | 15 |
| 1990 | 8 |
| 1991 | 7 |
| 1992 | 5 |
| 1993 | 51 |
| 1994 | 45 |
| 1995 | 3 |
| 1996 | 23 |
| 1997 | 517 |
| 1998 | 444 |
| 1999 | 13 |
| 2000 | 4 |
| 2001 | 4 |
| 2002 | 52 |
| 2003 | 8 |
| 2004 | 4 |
| 2005 | 8 |
| 2006 | 8 |
| 2007 | 5 |
| 2008 | 3 |
| 2009 | 201 |
| 2010 | 344 |
| 2011 | 13 |
| 2015 | 62 |
| 2017 | 1501 |
| 2018 | 909 |
| 2019 | 1 |
| 2020 | 1 |


### end_period (time)

| Value | Count |
|-------|-------|
| M01 | 1 |
| M02 | 3 |
| M03 | 15 |
| M04 | 5 |
| M05 | 11 |
| M06 | 5 |
| M07 | 348 |
| M08 | 3009 |
| M09 | 2 |
| M11 | 1 |
| M12 | 12 |
| M13 | 790 |
| S01 | 3059 |
| S02 | 1 |
| S03 | 841 |


### end_year (time)

| Value | Count |
|-------|-------|
| 1986 | 168 |
| 1997 | 53 |
| 1998 | 1 |
| 2000 | 2 |
| 2009 | 2 |
| 2016 | 1 |
| 2017 | 905 |
| 2018 | 4 |
| 2019 | 4 |
| 2020 | 12 |
| 2021 | 97 |
| 2022 | 10 |
| 2023 | 4 |
| 2024 | 411 |
| 2025 | 6429 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | cu.footnote|
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



