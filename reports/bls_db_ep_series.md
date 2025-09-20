# ep: Employment Projections

Report Date: 2025-09-19

## Series File

| Property | Value |
|----------|-------|
| filename | ep.series|
| size | 17.69 MB|
| #series | 113,473|
| #attributes | 17|
| variables | series_id, seasonal, occ_type, ind_type, occupation_code, industry_code, wkex_code, rank_code, otjt_code, eductrn_code, display_code, series_title, footnote_codes, begin_year, begin_period, end_year, end_period|


### Variables

Variables in the ep.series file

| column | count | unique | top | frequency |
|--------|-------|--------|-----|-----------|
| series_id | 113473 | 113473 | EPU000000110000 | 1 |
| seasonal | 113473 | 1 | U | 113473 |
| occ_type | 113473 | 2 | L | 67699 |
| ind_type | 113473 | 2 | L | 60786 |
| occupation_code | 113473 | 1113 | 00-0000 | 423 |
| industry_code | 113473 | 423 | TE1000 | 1113 |
| wkex_code | 113473 | 4 | 5 | 112641 |
| rank_code | 113473 | 1 | 1 | 113473 |
| otjt_code | 113473 | 7 | 7 | 112641 |
| eductrn_code | 113473 | 9 | 9 | 112641 |
| display_code | 113473 | 1 | 0 | 113473 |
| series_title | 113473 | 110331 | Cashiers in Educational services; state, local, and private | 4 |
| footnote_codes | 0 | 0 | N/A | 0 |
| begin_year | 113473 | 1 | 2024 | 113473 |
| begin_period | 113473 | 1 | A01 | 113473 |
| end_year | 113473 | 1 | 2024 | 113473 |
| end_period | 113473 | 1 | A01 | 113473 |


## Series ID Components

| Name | Class | Length | Regex |
|----------|-------|--------|-------|
| database_id | `A-Z` | `2` | `?P<database_id>[A-Z]{2}` |
| seasonal_code | `A-Z` | `1` | `?P<seasonal_code>[A-Z]{1}` |
| occupation_code | `\d` | `6` | `?P<occupation_code>[\d]{6}` |
| industry_code | `\d` | `6` | `?P<industry_code>[\d]{6}` |


### Component Codes

Code lists and attributes for series components



### seasonal_code

| Property | Value |
|----------|-------|
| filename | ep.seasonal|
| size | 0.08 KB|
| #codes | 2|
| variables | seasonal_code, seasonal_text|


#### Codes

| Value | Label |
|-------|-------|
| S | Seasonally Adjusted |
| U | Not Seasonally Adjusted |


### occupation_code

| Property | Value |
|----------|-------|
| filename | ep.occupation|
| size | 58.46 KB|
| #codes | 1,113|
| variables | occupation_code, occupation_title, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 000000 | Total, all occupations |
| 110000 | Management occupations |
| 111000 | Top executives |
| 111011 | Chief executives |
| 111021 | General and operations managers |
| 111031 | Legislators |
| 112000 | Advertising, marketing, promotions, public relations, and sales managers |
| 112011 | Advertising and promotions managers |
| 112020 | Marketing and sales managers |
| 112021 | Marketing managers |
| 112022 | Sales managers |
| 112030 | Public relations and fundraising managers |
| 112032 | Public relations managers |
| 112033 | Fundraising managers |
| 113000 | Operations specialties managers |
| 113010 | Administrative services and facilities managers |
| 113012 | Administrative services managers |
| 113013 | Facilities managers |
| 113021 | Computer and information systems managers |
| 113031 | Financial managers |
| ... | 1093 more codes |


### industry_code

| Property | Value |
|----------|-------|
| filename | ep.industry|
| size | 23.04 KB|
| #codes | 423|
| variables | industry_code, industry_title, display_level, selectable, sort_sequence|


#### Codes

| Value | Label |
|-------|-------|
| 110000 | Agriculture, forestry, fishing, and hunting |
| 111000 | Crop production |
| 112000 | Animal production and aquaculture |
| 113000 | Forestry and logging |
| 1131-2 | Forestry |
| 113300 | Logging |
| 114000 | Fishing, hunting and trapping |
| 115000 | Support activities for agriculture and forestry |
| 210000 | Mining, quarrying, and oil and gas extraction |
| 211000 | Oil and gas extraction |
| 212000 | Mining (except oil and gas) |
| 212100 | Coal mining |
| 212200 | Metal ore mining |
| 212300 | Nonmetallic mineral mining and quarrying |
| 213000 | Support activities for mining |
| 220000 | Utilities |
| 221000 | Utilities |
| 221100 | Electric power generation, transmission and distribution |
| 221110 | Electric power generation |
| 221111 | Hydroelectric power generation |
| ... | 403 more codes |


## Series Attributes

| Name | Type |
|------|------|
| begin_period | `time`|
| begin_year | `time`|
| display_code | `code`|
| eductrn_code | `code`|
| end_period | `time`|
| end_year | `time`|
| footnote_codes | `code`|
| ind_type | `other`|
| occ_type | `other`|
| otjt_code | `code`|
| rank_code | `code`|
| seasonal | `other`|
| series_title | `text`|
| wkex_code | `code`|


### begin_period (time)

| Value | Count |
|-------|-------|
| A01 | 113473 |


### begin_year (time)

| Value | Count |
|-------|-------|
| 2024 | 113473 |


### display_code (code)

| Property | Value |
|----------|-------|
| filename | ep.display|
| size | 0.05 KB|
| #codes | 1|
| variables | display_code, display_desc|


#### Codes

| Value | Label |
|-------|-------|
| 0 | Employment is on the record |


### eductrn_code (code)

| Property | Value |
|----------|-------|
| filename | ep.eductrn|
| size | 0.26 KB|
| #codes | 9|
| variables | eductrn_code, eductrn_desc|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Doctoral or professional degree |
| 2 | Master's degree |
| 3 | Bachelor's degree |
| 4 | Associate's degree |
| 5 | Postsecondary nondegree award |
| 6 | Some college, no degree |
| 7 | High school diploma or equivalent |
| 8 | No formal educational credential |
| 9 | - |


### end_period (time)

| Value | Count |
|-------|-------|
| A01 | 113473 |


### end_year (time)

| Value | Count |
|-------|-------|
| 2024 | 113473 |


### footnote_codes (code)

| Property | Value |
|----------|-------|
| filename | ep.footnote|
| size | 0.03 KB|
| #codes | 0|
| variables | footnote_code, footnote_text|


#### Codes

| Value | Label |
|-------|-------|


### ind_type (other)

No additional information available.



### occ_type (other)

No additional information available.



### otjt_code (code)

| Property | Value |
|----------|-------|
| filename | ep.otjt|
| size | 0.18 KB|
| #codes | 7|
| variables | otjt_code, otjt_text|


#### Codes

| Value | Label |
|-------|-------|
| 1 | Internship/residency |
| 2 | Apprenticeship |
| 3 | Long-term on-the-job training |
| 4 | Moderate-term on-the-job training |
| 5 | Short-term on-the-job training |
| 6 | nan |
| 7 | - |


### rank_code (code)

| Property | Value |
|----------|-------|
| filename | ep.rank|
| size | 0.03 KB|
| #codes | 1|
| variables | rank_code, rank_desc|


#### Codes

| Value | Label |
|-------|-------|
| 1 | n.a. |


### seasonal (other)

No additional information available.



### series_title (text)

No additional information available.



### wkex_code (code)

| Property | Value |
|----------|-------|
| filename | ep.wkex|
| size | 0.07 KB|
| #codes | 4|
| variables | wkex_code, wkex_text|


#### Codes

| Value | Label |
|-------|-------|
| 1 | 5 years or more |
| 2 | Less than 5 years |
| 4 | nan |
| 5 | - |


