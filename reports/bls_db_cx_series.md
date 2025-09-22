# cx: Consumer Expenditure Survey

Report Date: 2025-09-22

## Series File

| Property | Value |
|----------|-------|
| filename | cx.series|
| size | 29.31 MB|
| #series | 181,887|
| #attributes | 14|
| variables | series_id, seasonal, category_code, subcategory_code, item_code, demographics_code, characteristics_code, process_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the cx.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 181887 | 181887 | CXU001000LB0101M | 1 |
| seasonal | 181887 | 1 | U | 181887 |
| category_code | 181887 | 4 | EXPEND | 149825 |
| subcategory_code | 181887 | 23 | HOUSING | 43124 |
| item_code | 181887 | 1192 | 080110 | 164 |
| demographics_code | 181887 | 19 | LB02 | 25851 |
| characteristics_code | 181887 | 25 | 03 | 21954 |
| process_code | 181887 | 1 | M | 181887 |
| series_title | 181887 | 173317 | Income after taxes by Type of area: All Consumer Units | 7 |
| footnote_codes | 0 | 0 | N/A | 0 |
| begin_year | 181887 | 22 | 2010 | 105466 |
| begin_period | 181887 | 1 | A01 | 181887 |
| end_year | 181887 | 16 | 2023 | 114944 |
| end_period | 181887 | 1 | A01 | 181887 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| item_code | `\d` | `6` | `?P<item_code>[\d]{6}` |
| demographics_code | `A-Z0-9` | `4` | `?P<demographics_code>[A-Z0-9]{4}` |
| characteristics_code | `A-Z0-9` | `2` | `?P<characteristics_code>[A-Z0-9]{2}` |
| process_code | `A-Z` | `1` | `?P<process_code>[A-Z]{1}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

Codes file/list not available.

### item_code

| Property | Value |
|----------|-------|
| filename | cx.item|
| size | 67.51 KB|
| #codes | 1,198|
| variables | subcategory_code, item_code, item_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 200111 | Beer and ale |
| 200119 | Beer, ale, and other malt beverage |
| 200210 | Whiskey |
| 200219 | Distilled spirits |
| 200310 | Wine |
| 200410 | Other alcoholic beverages |
| 200511 | Beer and ale at fast food, carry out, delivery, concession stands, buffets, and cafeterias |
| 200512 | Beer and ale at full service restaurants |
| 200513 | Beer and ale at vending machines and mobile vendors |
| 200514 | Beer at employer |
| 200515 | Beer at board |
| 200516 | Beer and ale at catered affairs |
| 200521 | Wine at fast food, carry out, delivery, concession stands, buffets, and cafeterias |
| 200522 | Wine at full service restaurants |
| 200523 | Wine at vending machines and mobile vendors |
| 200524 | Wine at employer |
| 200525 | Wine at board |
| 200526 | Wine at catered affairs |
| 200531 | Other alcoholic beverages at fast food, carry out, delivery, concession stands, buffets, and cafeterias |
| 200532 | Other alcoholic beverages at full service restaurants |
| ... | 1178 more codes |


### demographics_code

| Property | Value |
|----------|-------|
| filename | cx.demographics|
| size | 0.84 KB|
| #codes | 19|
| variables | demographics_code, demographics_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| LB01 | Quintiles of income before taxes |
| LB02 | Income before taxes |
| LB04 | Age of reference person |
| LB05 | Size of consumer unit |
| LB06 | Composition of consumer unit |
| LB07 | Number of earners |
| LB09 | Race of reference person |
| LB10 | Hispanic or Latino origin of reference person |
| LB11 | Region of residence |
| LB12 | Occupation of reference person |
| LB13 | Education of reference person |
| LB14 | Highest education level of any member |
| LB15 | Deciles of income before taxes |
| LB16 | Generation of reference person |
| LB17 | Housing tenure |
| LB18 | Type of area |
| LB19 | Type of area |
| LB20 | Population size of area of residence |
| LB21 | Selected age of reference person |


### characteristics_code

| Property | Value |
|----------|-------|
| filename | cx.characteristics|
| size | 8.18 KB|
| #codes | 164|
| variables | demographics_code, characteristics_code, characteristics_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 01 | All Consumer Units |
| 02 | Lowest 20 percent income quintile |
| 03 | Second 20 percent income quintile |
| 04 | Third 20 percent income quintile |
| 05 | Fourth 20 percent income quintile |
| 06 | Highest 20 percent income quintile |
| A1 | Total complete income reporters |
| A2 | Incomplete income reports |
| 01 | All Consumer Units |
| 02 | Before tax income of less than $5,000 |
| 03 | $5,000 to $9,999 before tax income |
| 04 | $10,000 to $14,999 before tax income |
| 05 | $15,000 to $19,999 before tax income |
| 06 | $20,000 to $29,999 before tax income |
| 07 | $30,000 to $39,999 before tax income |
| 08 | $40,000 to $49,999 before tax income |
| 09 | $50,000 to $69,999 before tax income |
| 10 | Before tax income of $70,000 and over |
| 11 | Before tax income of less than $70,000(from 2003) |
| 12 | $70,000 to $79,999 before tax income(from 2003) |
| ... | 144 more codes |


### process_code

| Property | Value |
|----------|-------|
| filename | cx.process|
| size | 0.08 KB|
| #codes | 1|
| variables | process_code, process_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| M | Means |


## Series Attributes

| Name | Type |
|------|------|
| begin_period | `time`|
| begin_year | `time`|
| category_code | `code`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| seasonal | `other`|
| series_title | `text`|
| subcategory_code | `code`|


### begin_period (time)

| Value | Count |
|-------|-------|
| A01 | 181887 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1984 | 10425 |
| 1988 | 556 |
| 1990 | 154 |
| 1992 | 282 |
| 1994 | 282 |
| 1995 | 564 |
| 1996 | 564 |
| 2003 | 2115 |
| 2004 | 200 |
| 2010 | 105466 |
| 2011 | 1160 |
| 2012 | 9386 |
| 2013 | 7540 |
| 2014 | 12574 |
| 2015 | 6138 |
| 2016 | 5880 |
| 2017 | 2560 |
| 2019 | 3760 |
| 2020 | 128 |
| 2021 | 5753 |
| 2022 | 640 |
| 2023 | 5760 |


### category_code (code)

| Property | Value |
|----------|-------|
| filename | cx.category|
| size | 0.23 KB|
| #codes | 4|
| variables | category_code, category_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| ADDENDA | Assets and liabilities, and other financial info |
| CUCHARS | Consumer Characteristics |
| EXPEND | Expenditures |
| INCOME | Income and Taxes |


### end_period (time)

| Value | Count |
|-------|-------|
| A01 | 181887 |


### end_year (time)

| Value | Count |
|-------|-------|
| 1987 | 278 |
| 1991 | 141 |
| 2003 | 423 |
| 2009 | 4 |
| 2010 | 348 |
| 2011 | 928 |
| 2012 | 11822 |
| 2013 | 10801 |
| 2014 | 258 |
| 2015 | 12740 |
| 2017 | 896 |
| 2018 | 3479 |
| 2020 | 4985 |
| 2021 | 6016 |
| 2022 | 13824 |
| 2023 | 114944 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | cx.footnote|
| size | 0.98 KB|
| #codes | 9|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Components of income and taxes are derived from "complete income reporters" only through 2003; (see glossary). Beginning in 2004 income imputation was implemented. As a result, all consumer units are considered to be complete income reporters. |
| 2 | Expenses for other properties was moved from "Other lodging" to "Miscellaneous" in 1991. |
| 3 | Prior to 2005 this item was titled, 'Television, radios, sound equipment'. |
| 4 | See https://www.bls.gov/cex/2019-vehicle-insurance.htm regarding the 2019 increase in vehicle insurance expenditures. |
| 5 | Data are not available in LABSTAT. |
| 6 | Data are suppressed due to the Relative Standard Error (RSE) being equal to or greater than 25 percent. See www.bls.gov/cex/tables-getting-started-guide.htm for more information. |
| 7 | No data reported. |
| 8 | Value is too small to display. |
| 9 | For more information on the TAXSIM process and the models used to calculate these estimates see https://www.bls.gov/cex/tables-getting-started-guide.htm. |


### seasonal (other)

No additional information available.



### series_title (text)

No additional information available.



### subcategory_code (code)

| Property | Value |
|----------|-------|
| filename | cx.subcategory|
| size | 1.17 KB|
| #codes | 23|
| variables | category_code, subcategory_code, subcategory_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| CHGASLI | Net change in total assets and liabilities |
| TITLEOFI | Other financial informations: |
| CONSUNIT | Number of consumer units (in thousands) |
| TITLECU | Consumer unit characteristics: |
| TITLEPD | Percent distribution: |
| ALCBEVG | Alcoholic beverages |
| APPAREL | Apparel and services |
| CASHCONT | Cash contributions |
| EDUCATN | Education |
| ENTRTAIN | Entertainment |
| FOODTOTL | Food |
| HEALTH | Healthcare |
| HOUSING | Housing |
| INSPENSN | Personal insurance and pensions |
| MISC | Miscellaneous expenditures |
| PERSCARE | Personal care products and services |
| READING | Reading |
| TOBACCO | Tobacco products and smoking supplies |
| TOTALEXP | Total average annual expenditures |
| TRANS | Transportation |
| ... | 3 more codes |


