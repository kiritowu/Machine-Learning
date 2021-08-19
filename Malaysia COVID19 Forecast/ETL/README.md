The `etl.py` Script will Pull latest daily Malaysia Covid-19 data from the [covid19-public](https://github.com/MoH-Malaysia/covid19-public) Github Repo to perform **data-wrangling** and **output final** `malaysia_daily_stats_df.csv` file.

Data Dictionary:
1. **date** : Date of Covid Statistics
2. **cases_new** : Number of new cases reported in 24h since the last report
3. **deaths_new** : Number of new deaths due to COVID-19 reported in 24h since the last report
4. **total_test** : Sum of Number of test done using Antigen Rapid Test Kits (RTK-Ag) and Real-time Reverse Transcription Polymerase Chain Reaction (RT-PCR) technology
5. **checkins** : Number of checkins at all locations registered on MySejahtera
6. **unique_ind** : Number of unique accounts which checked in
7. **unique_loc** : Number of unique premises checked into
8. **casual_contacts** : Number of casual contacts identified and notified by CPRC's automated contact tracing system
9. **total_beds_available** : Sum of available hospital beds with related medical infrastructure and beds for non-critical care
10. **admitted_covid** : Number of individuals admitted to hospitals because of COVID-19
11. **discharged_covid** : Number of individuals discharged from hospitals because of COVID-19
12. **hosp_covid** : Number of individuals in hospitals currently because of COVID-19
13. **bed_icu_covid** : Total critical care beds dedicated for COVID-19
14. **icu_covid** : Total number of individuals under intensive care because of COVID-19
15. **vent_covid** : Total number of individuals on mechanical ventilation because of COVID-19