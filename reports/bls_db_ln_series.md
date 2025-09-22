# ln: Labor Force Statistics from the Current Population Survey (NAICS)

Report Date: 2025-09-22

## Series File

| Property | Value |
|----------|-------|
| filename | ln.series|
| size | 14.27 MB|
| #series | 67,244|
| #attributes | 42|
| variables | series_id, lfst_code, periodicity_code, series_title, absn_code, activity_code, ages_code, cert_code, class_code, duration_code, education_code, entr_code, expr_code, hheader_code, hour_code, indy_code, jdes_code, look_code, mari_code, mjhs_code, occupation_code, orig_code, pcts_code, race_code, rjnw_code, rnlf_code, rwns_code, seek_code, sexs_code, tdat_code, vets_code, wkst_code, born_code, chld_code, disa_code, seasonal, tlwk_code, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the ln.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 67244 | 67244 | LNS11000000 | 1 |
| lfst_code | 67244 | 34 | 20 | 38100 |
| periodicity_code | 67244 | 3 | A | 27063 |
| series_title | 67244 | 47767 | (Unadj) Employed - Service occupations, except protective occupations in Durable goods manufacturing industry, Asian | 4 |
| absn_code | 67244 | 4 | 0 | 66626 |
| activity_code | 67244 | 7 | 0 | 65398 |
| ages_code | 67244 | 35 | 00 | 33954 |
| cert_code | 67244 | 5 | 00 | 65768 |
| class_code | 67244 | 15 | 00 | 62429 |
| duration_code | 67244 | 11 | 000 | 65650 |
| education_code | 67244 | 12 | 00 | 63520 |
| entr_code | 67244 | 3 | 0 | 66912 |
| expr_code | 67244 | 3 | 0 | 64143 |
| hheader_code | 67244 | 2 | 00 | 67228 |
| hour_code | 67244 | 13 | 00 | 65758 |
| indy_code | 67244 | 342 | 0000 | 50800 |
| jdes_code | 67244 | 3 | 0 | 66730 |
| look_code | 67244 | 7 | 00 | 66585 |
| mari_code | 67244 | 8 | 00 | 63782 |
| mjhs_code | 67244 | 6 | 00 | 67022 |
| occupation_code | 67244 | 705 | 0000 | 48509 |
| orig_code | 67244 | 14 | 00 | 60158 |
| pcts_code | 67244 | 25 | 00 | 52321 |
| race_code | 67244 | 14 | 00 | 48661 |
| rjnw_code | 67244 | 15 | 00 | 66666 |
| rnlf_code | 67244 | 11 | 00 | 66874 |
| rwns_code | 67244 | 17 | 00 | 65740 |
| seek_code | 67244 | 2 | 00 | 66380 |
| sexs_code | 67244 | 3 | 0 | 42069 |
| tdat_code | 67244 | 8 | 00 | 39179 |
| vets_code | 67244 | 8 | 00 | 61460 |
| wkst_code | 67244 | 7 | 00 | 54574 |
| born_code | 67244 | 3 | 00 | 65824 |
| chld_code | 67244 | 6 | 00 | 65094 |
| disa_code | 67244 | 3 | 00 | 66334 |
| seasonal | 67244 | 2 | U | 66003 |
| tlwk_code | 67244 | 13 | 00 | 59184 |
| footnote_codes | 2 | 1 | 9 | 2 |
| begin_year | 67244 | 49 | 2022 | 9018 |
| begin_period | 67244 | 17 | A01 | 27081 |
| end_year | 67244 | 15 | 2025 | 40002 |
| end_period | 67244 | 11 | A01 | 27081 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| series_code | `\d` | `8` | `?P<series_code>[\d]{8}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | ln.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### series_code

Codes file/list not available.

## Series Attributes

| Name | Type |
|------|------|
| absn_code | `code`|
| activity_code | `code`|
| ages_code | `code`|
| begin_period | `time`|
| begin_year | `time`|
| born_code | `code`|
| cert_code | `code`|
| chld_code | `code`|
| class_code | `code`|
| disa_code | `code`|
| duration_code | `code`|
| education_code | `code`|
| end_period | `time`|
| end_year | `time`|
| entr_code | `code`|
| expr_code | `code`|
| footnote_codes | `code`|
| hheader_code | `code`|
| hour_code | `code`|
| indy_code | `code`|
| jdes_code | `code`|
| lfst_code | `code`|
| look_code | `code`|
| mari_code | `code`|
| mjhs_code | `code`|
| occupation_code | `code`|
| orig_code | `code`|
| pcts_code | `code`|
| periodicity_code | `code`|
| race_code | `code`|
| rjnw_code | `code`|
| rnlf_code | `code`|
| rwns_code | `code`|
| seasonal | `other`|
| seek_code | `code`|
| series_title | `text`|
| sexs_code | `code`|
| tdat_code | `code`|
| tlwk_code | `code`|
| vets_code | `code`|
| wkst_code | `code`|


### absn_code (code)

| Property | Value |
|----------|-------|
| filename | ln.absn|
| size | 0.10 KB|
| #codes | 5|
| variables | absn_code, absn_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Paid absence |
| 2 | Unpaid absence |
| 3 | Absence Universe |
| 4 | Lost-time Universe |


### activity_code (code)

| Property | Value |
|----------|-------|
| filename | ln.activity|
| size | 0.19 KB|
| #codes | 7|
| variables | activity_code, activity_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 3 | Enrolled in School |
| 4 | Enrolled in High School |
| 5 | Enrolled in College |
| 6 | Enrolled in College Full-time |
| 7 | Enrolled in College Part-time |
| 8 | Not Enrolled |


### ages_code (code)

| Property | Value |
|----------|-------|
| filename | ln.ages|
| size | 0.70 KB|
| #codes | 35|
| variables | ages_code, ages_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | 16 years and over |
| 1 | 14 years and over |
| 7 | 16 to 17 years |
| 8 | 16 to 19 years |
| 10 | 16 to 24 years |
| 11 | 16 to 64 years |
| 13 | 18 to 19 years |
| 15 | 18 years and over |
| 17 | 20 years and over |
| 20 | 20 to 24 years |
| 22 | 20 to 64 years |
| 28 | 25 years and over |
| 30 | 25 to 29 years |
| 31 | 25 to 34 years |
| 33 | 25 to 54 years |
| 36 | 30 to 34 years |
| 37 | 35 to 39 years |
| 38 | 35 to 44 years |
| 39 | 40 to 44 years |
| 40 | 45 years and over |
| ... | 15 more codes |


### begin_period (time)

| Value | Count |
|-------|-------|
| A01 | 27081 |
| M01 | 8828 |
| M02 | 127 |
| M03 | 23 |
| M04 | 4 |
| M05 | 888 |
| M06 | 2099 |
| M07 | 10 |
| M09 | 50 |
| M10 | 4513 |
| M11 | 97 |
| M12 | 2276 |
| M13 | 1138 |
| Q01 | 12835 |
| Q02 | 1503 |
| Q03 | 37 |
| Q04 | 5735 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 1940 | 10 |
| 1947 | 14 |
| 1948 | 1218 |
| 1954 | 546 |
| 1955 | 86 |
| 1963 | 48 |
| 1967 | 534 |
| 1968 | 170 |
| 1970 | 27 |
| 1972 | 1009 |
| 1973 | 98 |
| 1975 | 13 |
| 1976 | 2665 |
| 1977 | 21 |
| 1980 | 4 |
| 1981 | 149 |
| 1982 | 319 |
| 1983 | 160 |
| 1985 | 1478 |
| 1986 | 181 |
| 1987 | 40 |
| 1988 | 296 |
| 1989 | 13 |
| 1990 | 175 |
| 1992 | 494 |
| 1993 | 24 |
| 1994 | 2053 |
| 1999 | 4 |
| 2000 | 7796 |
| 2001 | 8 |
| 2002 | 11 |
| 2003 | 4935 |
| 2005 | 992 |
| 2006 | 2114 |
| 2007 | 228 |
| 2008 | 2612 |
| 2009 | 719 |
| 2010 | 7806 |
| 2011 | 262 |
| 2012 | 142 |
| 2013 | 1549 |
| 2014 | 6589 |
| 2015 | 2482 |
| 2016 | 274 |
| 2017 | 324 |
| 2020 | 2199 |
| 2022 | 9018 |
| 2023 | 5327 |
| 2025 | 8 |


### born_code (code)

| Property | Value |
|----------|-------|
| filename | ln.born|
| size | 0.20 KB|
| #codes | 13|
| variables | born_code, born_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Native born |
| 2 | Foreign born |
| 3 | Citizen |
| 4 | Non-citizen (Year of Entry) |
| 5 | Before 1965 |
| 6 | 1965-74 |
| 7 | 1975-84 |
| 8 | 1985-89 |
| 9 | 1990-94 |
| 10 | 1995-99 |
| 11 | 2000-04 |
| 12 | 2005 |


### cert_code (code)

| Property | Value |
|----------|-------|
| filename | ln.cert|
| size | 0.16 KB|
| #codes | 5|
| variables | cert_code, cert_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Without a certification or license |
| 2 | With a certification or license |
| 3 | With a certification, but no license |
| 4 | With a license |


### chld_code (code)

| Property | Value |
|----------|-------|
| filename | ln.chld|
| size | 0.19 KB|
| #codes | 6|
| variables | chld_code, chld_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | With own children under 18 |
| 2 | With own children 6 to 17, none younger |
| 3 | With own children under 6 |
| 4 | With own children under 3 |
| 5 | With no own children under 18 |


### class_code (code)

| Property | Value |
|----------|-------|
| filename | ln.class|
| size | 0.85 KB|
| #codes | 19|
| variables | class_code, class_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Wage and salary workers |
| 2 | Private wage and salary workers |
| 3 | Government wage and salary workers |
| 4 | Federal wage and salary workers |
| 5 | State wage and salary workers |
| 6 | Local wage and salary workers |
| 7 | State and local wage and salary workers |
| 8 | Self-employed workers, unincorporated |
| 9 | Unpaid family workers |
| 10 | All classes of workers (1, 8, and 9) |
| 11 | Nonagriculture government, self employed, and unpaid family worker (3, 8, and 9 above) |
| 12 | Self-employed unincorporated, and unpaid family workers (8 and 9) |
| 13 | Wage and salary and self-employed workers ('paid' workers-- 1 and 8) |
| 14 | Incorporated self-employed |
| 15 | Other |
| 16 | Wage and salary workers, excluding incorporated self employed |
| 17 | Private wage and salary workers, excluding incorporated self employed |
| 20 | Self-employed workers (both incorporated and unincorporated) |


### disa_code (code)

| Property | Value |
|----------|-------|
| filename | ln.disa|
| size | 0.06 KB|
| #codes | 3|
| variables | disa_code, disa_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Not disabled |
| 2 | Disabled person |


### duration_code (code)

| Property | Value |
|----------|-------|
| filename | ln.duration|
| size | 0.28 KB|
| #codes | 13|
| variables | duration_code, duration_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 6 | Less than 5 weeks |
| 18 | 15 weeks and over |
| 31 | 27 weeks and over |
| 58 | 52 weeks and over |
| 105 | 99 weeks and over |
| 106 | 5 to 10 weeks |
| 107 | 5 to 14 weeks |
| 108 | 11 to 14 weeks |
| 109 | 15 to 26 weeks |
| 110 | 27 to 51 weeks |
| 111 | 5 to 6 weeks |
| 112 | 7 to 10 weeks |


### education_code (code)

| Property | Value |
|----------|-------|
| filename | ln.education|
| size | 0.99 KB|
| #codes | 27|
| variables | education_code, education_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | All educational levels |
| 10 | Some High School or High School Graduate |
| 11 | Less than a High School diploma |
| 12 | Less than 1 year of High School |
| 16 | 4 years of High School, no diploma |
| 19 | High School graduates, no college |
| 20 | Some college or associate degree |
| 21 | Some college, no degree |
| 25 | Associate degree |
| 26 | Associate degree, occupational program |
| 27 | Associate degree, academic program |
| 30 | Less than a high school diploma (discontinued) |
| 31 | High school graduates, no college (discontinued) |
| 32 | Some college, no degree (discontinued) |
| 33 | College graduates (discontinued) |
| 34 | Associate degree (discontinued) |
| 35 | Less than a bachelor's degree (discontinued) |
| 36 | Some college or associate degree (discontinued) |
| 37 | Bachelor's degree only (discontinued) |
| 38 | Advanced degree (discontinued) |
| ... | 7 more codes |


### end_period (time)

| Value | Count |
|-------|-------|
| A01 | 27081 |
| M05 | 7 |
| M06 | 9 |
| M07 | 1 |
| M08 | 19953 |
| M12 | 12 |
| M13 | 71 |
| Q01 | 4 |
| Q02 | 20057 |
| Q03 | 4 |
| Q04 | 45 |


### end_year (time)

| Value | Count |
|-------|-------|
| 1947 | 10 |
| 1999 | 6 |
| 2002 | 28 |
| 2005 | 3 |
| 2008 | 8 |
| 2012 | 18 |
| 2013 | 8 |
| 2015 | 3 |
| 2016 | 52 |
| 2017 | 27 |
| 2018 | 6 |
| 2019 | 1491 |
| 2021 | 18 |
| 2024 | 25564 |
| 2025 | 40002 |


### entr_code (code)

| Property | Value |
|----------|-------|
| filename | ln.entr|
| size | 0.06 KB|
| #codes | 3|
| variables | entr_code, entr_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Reentrants |
| 2 | New entrants |


### expr_code (code)

| Property | Value |
|----------|-------|
| filename | ln.expr|
| size | 0.07 KB|
| #codes | 3|
| variables | expr_code, expr_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Experienced |
| 2 | No previous work experience |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | ln.footnote|
| size | 0.78 KB|
| #codes | 8|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Data affected by changes in population controls. |
| 2 | Constructed on the 2002 Census Industry Classification from data originally coded on earlier classifications. Official series was not revised. |
| 3 | 2000 forward coded on the 2002 Census Occupation Classification. 1983-99 constructed from data originally coded on earlier classifications. |
| 4 | 2000 forward coded on the 2002 Census Industry Classification. 1983-99 constructed from data originally coded on earlier classifications. |
| 7 | Data do not meet publication criteria. |
| 8 | This series id code has been discontinued; data are available using the database tool at www.bls.gov/webapps/legacy/cpsatab8.htm. |
| 9 | Data from 1994 through 2002 were revised in February 2014 with updated seasonal adjustments. |
| C | Corrected |


### hheader_code (code)

| Property | Value |
|----------|-------|
| filename | ln.hheader|
| size | 0.05 KB|
| #codes | 2|
| variables | hheader_code, hheader_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Family heads |


### hour_code (code)

| Property | Value |
|----------|-------|
| filename | ln.hour|
| size | 0.25 KB|
| #codes | 13|
| variables | hour_code, hour_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | 1 to 34 hours |
| 2 | 1 to 4 hours |
| 6 | 5 to 14 hours |
| 10 | 15 to 29 hours |
| 14 | 30 to 34 hours |
| 16 | 35 hours and over |
| 17 | 35 to 39 hours |
| 20 | 40 hours |
| 21 | 41 hours and over |
| 23 | 41 to 48 hours |
| 27 | 49 to 59 hours |
| 29 | 60 hours and over |


### indy_code (code)

| Property | Value |
|----------|-------|
| filename | ln.indy|
| size | 15.20 KB|
| #codes | 358|
| variables | indy_code, indy_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | All Industries |
| 168 | Agriculture and related industries |
| 169 | Agriculture, forestry, fishing, and hunting |
| 170 | Crop production |
| 180 | Animal production and aquaculture |
| 188 | Nonfarm Industries |
| 190 | Forestry, except logging |
| 270 | Logging |
| 280 | Fishing, hunting, and trapping |
| 290 | Support activities for agriculture and forestry |
| 368 | Nonagriculture industries |
| 369 | Mining, quarrying, and oil and gas extraction |
| 370 | Oil and gas extraction |
| 380 | Coal mining |
| 390 | Metal ore mining |
| 470 | Nonmetallic mineral mining and quarrying |
| 480 | Not specified type of mining |
| 490 | Support activities for mining |
| 569 | Utilities |
| 570 | Electric power generation, transmission, and distribution |
| ... | 338 more codes |


### jdes_code (code)

| Property | Value |
|----------|-------|
| filename | ln.jdes|
| size | 0.07 KB|
| #codes | 3|
| variables | jdes_code, jdes_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Want a job now |
| 2 | Don't want a job now |


### lfst_code (code)

| Property | Value |
|----------|-------|
| filename | ln.lfst|
| size | 2.38 KB|
| #codes | 52|
| variables | lfst_code, lfst_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | Civilian noninstitutional population |
| 10 | Civilian labor force |
| 11 | Full time labor force (includes persons working part time for economic reasons, both usually work fu |
| 12 | Part time labor force (excludes persons working part time for economic reasons) |
| 13 | Civilian labor force participation rate |
| 14 | Percent of labor force time lost |
| 15 | Experienced labor force |
| 16 | Civilian Labor Force plus discouraged workers |
| 17 | Civilian Labor Force plus marginally attached workers |
| 20 | Employed |
| 21 | Employed full time (includes persons working part time for economic reasons) |
| 22 | Employed part time (by economic/noneconomic reason) |
| 23 | Employment-population ratio |
| 24 | Employed part time (involuntary) |
| 25 | Employed full time (persons who usually work 35 hours or more) |
| 26 | Employed part time (persons who usually work less than 35 hours) |
| 27 | Aggregated totals employed |
| 28 | Employment-population ratio (Full-time Workers) |
| 29 | Employment-population ratio (Part-time Workers) |
| 30 | Unemployed |
| ... | 32 more codes |


### look_code (code)

| Property | Value |
|----------|-------|
| filename | ln.look|
| size | 0.76 KB|
| #codes | 24|
| variables | look_code, look_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Job losers and persons who completed temporary jobs |
| 2 | Total on layoff |
| 3 | Temporary layoff |
| 4 | Indefinite layoff |
| 5 | All other job losers |
| 6 | Quit job (job leavers) |
| 7 | Other reasons (than 1 and 6) |
| 8 | Left school |
| 9 | Want temporary work |
| 10 | Other reasons (than 8 and 9) left last job |
| 12 | Personal, family, or school |
| 13 | Ill health, disability |
| 14 | Retirement, old age |
| 15 | Seasonal job completed |
| 16 | Slack work or business conditions |
| 17 | Temporary job completed (nonseasonal) |
| 18 | Unsatisfactory work arrangements |
| 19 | Reasons (other than 12,13,14,15,16,17,and 18) |
| 20 | Total economic reasons (15, 16, and 17) |
| ... | 4 more codes |


### mari_code (code)

| Property | Value |
|----------|-------|
| filename | ln.mari|
| size | 0.38 KB|
| #codes | 11|
| variables | mari_code, mari_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Never married |
| 2 | Married, spouse present |
| 3 | Civilian spouse present |
| 5 | Separated (including married, spouse absent) |
| 6 | Widowed |
| 7 | Divorced |
| 8 | Widowed and divorced |
| 9 | Widowed, divorced, and separated (including married, spouse absent) |
| 10 | Married (codes 2 and 5) |
| 11 | Never married, widowed, divorced, and separated (including married, spouse absent) |


### mjhs_code (code)

| Property | Value |
|----------|-------|
| filename | ln.mjhs|
| size | 0.32 KB|
| #codes | 6|
| variables | mjhs_code, mjhs_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Multiple job holders |
| 2 | Multiple job holders, primary job full time, secondary job part time |
| 3 | Multiple job holders, primary and secondary job both part time |
| 4 | Multiple job holders, primary and secondary job both full time |
| 5 | Multiple job holders, hours vary on primary or secondary job |


### occupation_code (code)

| Property | Value |
|----------|-------|
| filename | ln.occupation|
| size | 31.54 KB|
| #codes | 760|
| variables | occupation_code, occupation_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | All Occupations |
| 7 | Management, professional and related occupations |
| 8 | Management, business, and financial operations occupations |
| 9 | Management occupations |
| 10 | Chief executives |
| 20 | General and operations managers |
| 30 | Legislators |
| 40 | Advertising and promotions managers |
| 50 | Marketing and sales managers |
| 51 | Marketing managers |
| 52 | Sales managers |
| 60 | Public relations and fundraising managers |
| 100 | Administrative services managers |
| 101 | Administrative services managers |
| 102 | Facilities managers |
| 110 | Computer and information systems managers |
| 120 | Financial managers |
| 130 | Human resources managers |
| 135 | Compensation and benefits managers |
| 136 | Human resources managers |
| ... | 740 more codes |


### orig_code (code)

| Property | Value |
|----------|-------|
| filename | ln.orig|
| size | 0.45 KB|
| #codes | 17|
| variables | orig_code, orig_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | All Origins |
| 1 | Hispanic or Latino |
| 2 | Mexican |
| 5 | Mexican (discontinued) |
| 6 | Puerto Rican |
| 7 | Cuban |
| 8 | Central or South American (discontinued) |
| 9 | Other Hispanic or Latino (discontinued) |
| 10 | Non-Hispanic |
| 15 | Central or South American |
| 20 | Central American |
| 21 | Salvadoran |
| 25 | Other Central American (excludes Salvadoran) |
| 30 | South American |
| 40 | Other Hispanic or Latino |
| 41 | Dominican |
| 45 | Other Hispanic or Latino (excludes Dominican) |


### pcts_code (code)

| Property | Value |
|----------|-------|
| filename | ln.pcts|
| size | 1.35 KB|
| #codes | 30|
| variables | pcts_code, pcts_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Percent of civilian noninstitutional population |
| 2 | Percent of civilian noninstitutional population |
| 3 | Percent of civilian labor force |
| 4 | Percent of not in labor force |
| 5 | Percent of employed within group |
| 6 | Percent of total employed |
| 7 | Percent of total unemployed |
| 8 | Percent of unemployed within group |
| 11 | Percent of total job seekers |
| 18 | Percent of total job losers |
| 19 | Percent of total job leavers |
| 20 | Percent of total reentrants |
| 21 | Percent of total new entrants |
| 24 | Percent of employed in all agri industries |
| 25 | Percent of employed in all nonagri industries |
| 26 | Percent of at work in all nonagri industries |
| 27 | Percent of at work in all agri industries |
| 33 | Percent of employed by industry |
| 34 | Percent of employed by occupation |
| ... | 10 more codes |


### periodicity_code (code)

| Property | Value |
|----------|-------|
| filename | ln.periodicity|
| size | 0.07 KB|
| #codes | 3|
| variables | periodicity_code, periodicity_text|


#### Codes

| Value | Label |
|-------|-------|
| A | Annual |
| M | Monthly |
| Q | Quarterly |


### race_code (code)

| Property | Value |
|----------|-------|
| filename | ln.race|
| size | 0.33 KB|
| #codes | 14|
| variables | race_code, race_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | All Races |
| 1 | White |
| 3 | Black or African American |
| 4 | Asian |
| 5 | American Indian or Alaska Native |
| 6 | Native Hawaiian or Other Pacific Islander |
| 7 | Two or more races |
| 10 | Asian - Asian Indian |
| 15 | Asian - Chinese |
| 25 | Asian - Filipino |
| 26 | Asian - Japanese |
| 27 | Asian - Korean |
| 28 | Asian - Vietnamese |
| 30 | Asian - Other Asian |


### rjnw_code (code)

| Property | Value |
|----------|-------|
| filename | ln.rjnw|
| size | 0.79 KB|
| #codes | 17|
| variables | rjnw_code, rjnw_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Own illness, injury, or medical problems |
| 2 | Vacation or personal days |
| 3 | Weather affected job (bad weather) |
| 4 | Labor dispute |
| 5 | All reasons other than own illness, vacation, bad weather, or labor dispute |
| 6 | All reasons other than own illness or vacation |
| 7 | Other reasons (than 1 and 2) |
| 8 | Child care problems, maternity/paternity leave, or other family/personal obligations |
| 20 | Own illness/injury, Child care problems, other personal obligations, maternity leave, or civic duty |
| 21 | Child care problems, other personal obligation, maternity/paternity leave, or civic/military duty |
| 30 | Childcare problems |
| 31 | Other family or personal obligations |
| 32 | Maternity or paternity leave |
| 33 | School or training |
| 34 | Civic or military duty |
| 35 | Other reasons, not elsewhere classified |


### rnlf_code (code)

| Property | Value |
|----------|-------|
| filename | ln.rnlf|
| size | 0.66 KB|
| #codes | 11|
| variables | rnlf_code, rnlf_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 60 | Did not search for work in previous year |
| 61 | Searched for work in previous year - Total |
| 62 | Searched for work in previous year - Not available to work now |
| 63 | Searched for work in previous year - Available to work now (Marginally attached) |
| 64 | Discouragement over job prospects (believes no job is available) |
| 65 | Reasons other than discouragement - Total |
| 66 | Reasons other than discouragement - Family responsibilities |
| 67 | Reasons other than discouragement - In school or training |
| 68 | Reasons other than discouragement - Ill health or disability |
| 69 | Reasons other than discouragement - Other (child care, transportation problems, other reasons) |


### rwns_code (code)

| Property | Value |
|----------|-------|
| filename | ln.rwns|
| size | 0.86 KB|
| #codes | 27|
| variables | rwns_code, rwns_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Economic reasons |
| 2 | Slack work |
| 3 | Material shortage |
| 4 | Plant or machine repair |
| 5 | Job started during week |
| 6 | Job terminated during week |
| 7 | Could only find part time work |
| 8 | Other economic reasons (than 2 through 7) |
| 9 | Material shortages and repairs to plant and equipment |
| 10 | Noneconomic reasons |
| 11 | Labor dispute |
| 12 | Holiday (legal or religious) |
| 13 | Bad weather |
| 14 | Illness |
| 15 | Vacation |
| 16 | Personal reasons (business, home or school) |
| 17 | Do not want, or unavailable for, full time work |
| 18 | Full-time work week under 35 hours |
| 30 | Child-care problems |
| ... | 7 more codes |


### seasonal (other)

No additional information available.



### seek_code (code)

| Property | Value |
|----------|-------|
| filename | ln.seek|
| size | 0.06 KB|
| #codes | 2|
| variables | seek_code, seek_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Job Seeker (Looking for work) |


### series_title (text)

No additional information available.



### sexs_code (code)

| Property | Value |
|----------|-------|
| filename | ln.sexs|
| size | 0.05 KB|
| #codes | 3|
| variables | sexs_code, sexs_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | Both Sexes |
| 1 | Men |
| 2 | Women |


### tdat_code (code)

| Property | Value |
|----------|-------|
| filename | ln.tdat|
| size | 0.60 KB|
| #codes | 20|
| variables | tdat_code, tdat_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | Number in thousands |
| 1 | Percent or rate |
| 2 | Average weeks |
| 3 | Median weeks |
| 4 | Average hours at work |
| 5 | Median hours at work |
| 6 | Average years |
| 7 | Median years |
| 8 | Average number of methods used for seeking jobs |
| 9 | Total methods used for seeking jobs |
| 10 | hours at work worked |
| 11 | hours at work offered |
| 12 | hours at work lost |
| 13 | Aggregate-hours at work |
| 14 | Aggregate-weeks |
| 15 | Aggregate weeks of unemployment |
| 16 | Number of families |
| 17 | Aggregate usual hours |
| 18 | Average weekly hours teleworked or worked at home for pay |
| 19 | Aggregate weekly hours teleworked or worked at home for pay |


### tlwk_code (code)

| Property | Value |
|----------|-------|
| filename | ln.tlwk|
| size | 0.56 KB|
| #codes | 13|
| variables | tlwk_code, tlwk_text, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Persons who teleworked or worked at home for pay |
| 2 | Persons who teleworked or worked at home for pay, Teleworked some hours |
| 3 | Persons who teleworked or worked at home for pay, Teleworked all hours |
| 4 | Persons who did not telework or work at home for pay |
| 5 | Teleworked, Up to 8 hours |
| 6 | Teleworked, 9 to 16 hours |
| 7 | Teleworked, 17 to 24 hours |
| 8 | Teleworked, 25 to 32 hours |
| 9 | Teleworked, 33 to 39 hours |
| 10 | Teleworked, 40 hours or more |
| 11 | Teleworked, 40 hours |
| 12 | Teleworked, 41 hours or more |


### vets_code (code)

| Property | Value |
|----------|-------|
| filename | ln.vets|
| size | 0.30 KB|
| #codes | 8|
| variables | vets_code, vets_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | Veteran |
| 3 | Vietnam era and earlier wartime periods |
| 9 | Gulf War Era |
| 12 | Veterans who served in Gulf War Era 2 (whether or not they served in Era 1) |
| 13 | Veterans who served in Gulf War Era 1 but not Gulf War Era 2 |
| 16 | Other Service Periods (may include peacetime) |
| 25 | Nonveteran |


### wkst_code (code)

| Property | Value |
|----------|-------|
| filename | ln.wkst|
| size | 0.48 KB|
| #codes | 12|
| variables | wkst_code, wkst_text|


#### Codes

| Value | Label |
|-------|-------|
| 0 | nan |
| 1 | At work |
| 2 | At work part time |
| 3 | At work part time, usually work full time |
| 4 | At work part time, usually work part time |
| 5 | At work on full time schedules  (only use to distinguish >35 hrs) |
| 7 | With a job not at work |
| 8 | Usually work full-time schedules (with a job not at work) |
| 9 | Usually work part-time schedules (with a job not at work) |
| 19 | At work full time |
| 20 | At work 35+ hours, usually work part time |
| 21 | At work 35+ hours, usually work full time |


