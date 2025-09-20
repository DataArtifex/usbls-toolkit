# ap: Average Price Data

Report Date: 2025-09-19

## Series File

| Property | Value |
|----------|-------|
| filename | ap.series|
| size | 225.49 KB|
| #series | 1,482|
| #attributes | 9|
| variables | series_id, area_code, item_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the ap.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 1482 | 1482 | APU0000701111 | 1 |
| area_code | 1482 | 74 | 0000 | 160 |
| item_code | 1482 | 160 | 72610 | 74 |
| series_title | 1482 | 1482 | All Ham (Excluding Canned Ham and Luncheon Slices), per lb. (453.6 gm) in Midwest urban, average price, not seasonally adjusted | 1 |
| footnote_codes | 0 | 0 | N/A | 0 |
| begin_year | 1482 | 30 | 1978 | 494 |
| begin_period | 1482 | 12 | M01 | 935 |
| end_year | 1482 | 46 | 2025 | 439 |
| end_period | 1482 | 12 | M12 | 471 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| item_code | `\d` | `4` | `?P<item_code>[\d]{4}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | ap.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### item_code

| Property | Value |
|----------|-------|
| filename | ap.item|
| size | 9.03 KB|
| #codes | 160|
| variables | item_code, item_name|


#### Codes

| Value | Label |
|-------|-------|
| 701111 | Flour, white, all purpose, per lb. (453.6 gm) |
| 701311 | Rice, white, long grain, precooked (cost per pound/453.6 grams) |
| 701312 | Rice, white, long grain, uncooked, per lb. (453.6 gm) |
| 701321 | Spaghetti (cost per pound/453.6 grams) |
| 701322 | Spaghetti and macaroni, per lb. (453.6 gm) |
| 702111 | Bread, white, pan, per lb. (453.6 gm) |
| 702112 | Bread, French, per lb. (453.6 gm) |
| 702211 | Bread, rye, pan (cost per pound/453.6 grams) |
| 702212 | Bread, whole wheat, pan, per lb. (453.6 gm) |
| 702213 | Bread, wheat blend, pan (cost per pound/453.6 grams) |
| 702221 | Rolls, hamburger (cost per pound/453.6 grams) |
| 702411 | Cupcakes, chocolate (cost per pound/453.6 grams) |
| 702421 | Cookies, chocolate chip, per lb. (453.6 gm) |
| 702611 | Crackers, soda, salted, per lb. (453.6 gm) |
| 703111 | Ground chuck, 100% beef, per lb. (453.6 gm) |
| 703112 | Ground beef, 100% beef, per lb. (453.6 gm) |
| 703113 | Ground beef, lean and extra lean, per lb. (453.6 gm) |
| 703211 | Chuck roast, USDA Choice, bone-in, per lb. (453.6 gm) |
| 703212 | Chuck roast, graded and ungraded, excluding USDA Prime and Choice, per lb. (453.6 gm) |
| 703213 | Chuck roast, USDA Choice, boneless, per lb. (453.6 gm) |
| ... | 140 more codes |


## Series Attributes

| Name | Type |
|------|------|
| area_code | `code`|
| begin_period | `time`|
| begin_year | `time`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| series_title | `text`|


### area_code (code)

| Property | Value |
|----------|-------|
| filename | ap.area|
| size | 2.06 KB|
| #codes | 74|
| variables | area_code, area_name|


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
| A105 | Buffalo-Niagara Falls, NY |
| A106 | Scranton, PA |
| A210 | Cleveland-Akron, OH |
| A212 | Milwaukee-Racine, WI |
| A213 | Cincinnati-Hamilton, OH-KY-IN |
| ... | 54 more codes |


### begin_period (time)

| Value | Count |
|-------|-------|
| M01 | 935 |
| M02 | 7 |
| M03 | 12 |
| M04 | 31 |
| M05 | 9 |
| M06 | 19 |
| M07 | 55 |
| M08 | 8 |
| M09 | 49 |
| M10 | 7 |
| M11 | 299 |
| M12 | 51 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1973 | 2 |
| 1976 | 1 |
| 1978 | 494 |
| 1979 | 8 |
| 1980 | 428 |
| 1981 | 50 |
| 1982 | 1 |
| 1983 | 2 |
| 1984 | 44 |
| 1985 | 8 |
| 1986 | 7 |
| 1987 | 45 |
| 1988 | 1 |
| 1989 | 10 |
| 1991 | 34 |
| 1992 | 3 |
| 1993 | 40 |
| 1994 | 3 |
| 1995 | 51 |
| 1996 | 2 |
| 1998 | 115 |
| 2002 | 2 |
| 2004 | 3 |
| 2005 | 1 |
| 2006 | 9 |
| 2007 | 1 |
| 2012 | 1 |
| 2014 | 1 |
| 2018 | 112 |
| 2021 | 3 |


### end_period (time)

| Value | Count |
|-------|-------|
| M01 | 26 |
| M02 | 40 |
| M03 | 33 |
| M04 | 72 |
| M05 | 48 |
| M06 | 124 |
| M07 | 56 |
| M08 | 440 |
| M09 | 70 |
| M10 | 77 |
| M11 | 25 |
| M12 | 471 |


### end_year (time)

| Value | Count |
|-------|-------|
| 1980 | 33 |
| 1981 | 48 |
| 1982 | 11 |
| 1983 | 17 |
| 1984 | 11 |
| 1985 | 17 |
| 1986 | 145 |
| 1987 | 19 |
| 1988 | 45 |
| 1989 | 22 |
| 1990 | 18 |
| 1991 | 27 |
| 1992 | 10 |
| 1993 | 5 |
| 1994 | 6 |
| 1995 | 7 |
| 1996 | 6 |
| 1997 | 173 |
| 1998 | 1 |
| 1999 | 4 |
| 2000 | 11 |
| 2001 | 4 |
| 2002 | 8 |
| 2003 | 6 |
| 2004 | 5 |
| 2005 | 4 |
| 2006 | 3 |
| 2007 | 2 |
| 2008 | 3 |
| 2009 | 5 |
| 2010 | 3 |
| 2011 | 4 |
| 2012 | 11 |
| 2013 | 107 |
| 2014 | 7 |
| 2015 | 4 |
| 2016 | 8 |
| 2017 | 54 |
| 2018 | 8 |
| 2019 | 16 |
| 2020 | 20 |
| 2021 | 4 |
| 2022 | 12 |
| 2023 | 4 |
| 2024 | 105 |
| 2025 | 439 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | ap.footnote|
| size | 0.03 KB|
| #codes | 0|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|


### series_title (text)

No additional information available.



