# ei: International Price Index

Report Date: 2025-09-22

## Series File

| Property | Value |
|----------|-------|
| filename | ei.series|
| size | 371.20 KB|
| #series | 1,625|
| #attributes | 11|
| variables | series_id, seasonal, index_code, series_name, base_period, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the ei.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 1625 | 1625 | EIUCDCANMANU | 1 |
| seasonal | 1625 | 1 | U | 1625 |
| index_code | 1625 | 13 | IZ | 345 |
| series_name | 1625 | 1280 | Miscellaneous manufactured articles | 3 |
| base_period | 1625 | 29 | January 2025=100 | 548 |
| series_title | 1625 | 1625 | Monthly export price index by destination for NAICS, All industries, Canada, not seasonally adjusted | 1 |
| footnote_codes | 12 | 6 | 2 | 3 |
| begin_year | 1625 | 45 | 2025 | 548 |
| begin_period | 1625 | 5 | M12 | 872 |
| end_year | 1625 | 1 | 2025 | 1625 |
| end_period | 1625 | 1 | M08 | 1625 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| index_code | `A-Z` | `2` | `?P<index_code>[A-Z]{2}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | ei.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### index_code

| Property | Value |
|----------|-------|
| filename | ei.index|
| size | 0.48 KB|
| #codes | 13|
| variables | index_code, index_name|


#### Codes

| Value | Label |
|-------|-------|
| CD | Locality of Destination Price Indexes |
| CO | Locality of Origin Price Indexes |
| CT | Terms of Trade Indexes |
| IC | Services Inbound Price Indexes |
| ID | Harmonized System Export Price Indexes |
| IH | Services Export Price Indexes |
| IP | Harmonized System Import Price Indexes |
| IQ | BEA End Use Export Price Indexes |
| IR | BEA End Use Import Price Indexes |
| IS | Services Outbound Price Indexes |
| IV | Services Import Price Indexes |
| IY | NAICS Export Price Indexes |
| IZ | NAICS Import Price Indexes |


## Series Attributes

| Name | Type |
|------|------|
| base_period | `time`|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| seasonal | `other`|
| series_name | `text`|
| series_title | `text`|


### base_period (time)

| Value | Count |
|-------|-------|
| 2000=100 | 302 |
| December 2001=100 | 12 |
| December 2002=100 | 4 |
| December 2003=100 | 13 |
| December 2004=100 | 4 |
| December 2005=100 | 116 |
| December 2006=100 | 6 |
| December 2007=100 | 9 |
| December 2008=100 | 6 |
| December 2009=100 | 10 |
| December 2010=100 | 3 |
| December 2011=100 | 1 |
| December 2012=100 | 7 |
| December 2013=100 | 5 |
| December 2014=100 | 6 |
| December 2015=100 | 2 |
| December 2016=100 | 8 |
| December 2017=100 | 41 |
| December 2018=100 | 28 |
| December 2019=100 | 55 |
| December 2020=100 | 37 |
| December 2021=100 | 23 |
| December 2022=100 | 43 |
| December 2023=100 | 124 |
| December 2024=100 | 65 |
| January 2025=100 | 548 |
| June 2012=100 | 145 |
| June 2022=100 | 1 |
| March 2003=100 | 1 |


### begin_period (time)

| Value | Count |
|-------|-------|
| M01 | 548 |
| M03 | 19 |
| M06 | 155 |
| M09 | 31 |
| M12 | 872 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1977 | 1 |
| 1978 | 1 |
| 1979 | 4 |
| 1980 | 29 |
| 1981 | 11 |
| 1982 | 6 |
| 1983 | 15 |
| 1984 | 71 |
| 1985 | 5 |
| 1986 | 5 |
| 1987 | 3 |
| 1988 | 2 |
| 1989 | 5 |
| 1990 | 14 |
| 1992 | 111 |
| 1993 | 2 |
| 1994 | 3 |
| 1996 | 12 |
| 1997 | 3 |
| 1998 | 2 |
| 2001 | 13 |
| 2002 | 4 |
| 2003 | 14 |
| 2004 | 4 |
| 2005 | 116 |
| 2006 | 6 |
| 2007 | 9 |
| 2008 | 6 |
| 2009 | 10 |
| 2010 | 3 |
| 2011 | 1 |
| 2012 | 152 |
| 2013 | 5 |
| 2014 | 6 |
| 2015 | 2 |
| 2016 | 8 |
| 2017 | 41 |
| 2018 | 28 |
| 2019 | 55 |
| 2020 | 37 |
| 2021 | 23 |
| 2022 | 44 |
| 2023 | 124 |
| 2024 | 61 |
| 2025 | 548 |


### end_period (time)

| Value | Count |
|-------|-------|
| M08 | 1625 |


### end_year (time)

| Value | Count |
|-------|-------|
| 2025 | 1625 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | ei.footnote|
| size | 0.67 KB|
| #codes | 7|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| 2 | Western Europe, Canada, Japan, Australia, New Zealand, and South Africa. |
| 3 | Mexico, Central America, South America, and the Caribbean. |
| 4 | China, Japan, Australia, Brunei, Indonesia, Macao, Malaysia, New Zealand, Papua New Guinea, Philippines, and the Asian Newly Industrialized Countries. |
| 5 | Asian Newly Industrialized Countries - Hong Kong, Singapore, South Korea, and Taiwan. |
| 6 | Association of Southeast Asian Nations - Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, and Vietnam. |
| 7 | Bahrain, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Qatar, Saudi Arabia, Syria, United Arab Emirates, and Yemen. |
| R | Revised. |


### seasonal (other)

No additional information available.



### series_name (text)

No additional information available.



### series_title (text)

No additional information available.



