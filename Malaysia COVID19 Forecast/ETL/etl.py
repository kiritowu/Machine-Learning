'''
This Python Script will Pull latest Malaysia Covid-19 data from the 
covid19-public Github Repo : https://github.com/MoH-Malaysia/covid19-public
to perform data-wrangling and output final `malaysia_daily_stats_df.csv` file

Data Dictionary:
1. date : Date of Covid Statistics
2. cases_new : Number of new cases reported in 24h since the last report
3. deaths_new : Number of new deaths due to COVID-19 reported in 24h since the last report
4. total_test : Sum of Number of test done using Antigen Rapid Test Kits (RTK-Ag) and Real-time Reverse Transcription Polymerase Chain Reaction (RT-PCR) technology
5. checkins : Number of checkins at all locations registered on MySejahtera
6. unique_ind : Number of unique accounts which checked in
7. unique_loc : Number of unique premises checked into
8. casual_contacts : Number of casual contacts identified and notified by CPRC's automated contact tracing system
9. total_beds_available : Sum of available hospital beds with related medical infrastructure and beds for non-critical care
10. admitted_covid : Number of individuals admitted to hospitals because of COVID-19
11. discharged_covid : Number of individuals discharged from hospitals because of COVID-19
12. hosp_covid : Number of individuals in hospitals currently because of COVID-19
13. bed_icu_covid : Total critical care beds dedicated for COVID-19
14. icu_covid : Total number of individuals under intensive care because of COVID-19
15. vent_covid : Total number of individuals on mechanical ventilation because of COVID-19
'''

# Import Dependencies
import os
import git
import pandas as pd

# Folder Locations
BASE_FOLDER = "../covid19-public" 
EPIDEMIC_FOLDER = os.path.join(BASE_FOLDER, 'epidemic')
MYSEJAHTERA_FOLDER = os.path.join(BASE_FOLDER, 'mysejahtera')

# Pull Latest Data
g = git.Git(BASE_FOLDER)
g.pull('origin','main')

# Extract
# Importing Raw Files
## Covid Cases Details
cases_malaysia_df = pd.read_csv(os.path.join(EPIDEMIC_FOLDER, 'cases_malaysia.csv'))
deaths_malaysia_df = pd.read_csv(os.path.join(EPIDEMIC_FOLDER, 'deaths_malaysia.csv'))
tests_malaysia_df = pd.read_csv(os.path.join(EPIDEMIC_FOLDER, 'tests_malaysia.csv'))
## Hospital Capacity Details
hospital_df = pd.read_csv(os.path.join(EPIDEMIC_FOLDER, 'hospital.csv'))
icu_df = pd.read_csv(os.path.join(EPIDEMIC_FOLDER, 'icu.csv'))
## Mysejahtera Details
checkin_malaysia_df = pd.read_csv(os.path.join(MYSEJAHTERA_FOLDER, 'checkin_malaysia.csv'))
trace_malaysia_df = pd.read_csv(os.path.join(MYSEJAHTERA_FOLDER, 'trace_malaysia.csv'))

# Turn date column into datetime index
cases_malaysia_df.index = pd.to_datetime(cases_malaysia_df.date)
deaths_malaysia_df.index = pd.to_datetime(deaths_malaysia_df.date)
tests_malaysia_df.index = pd.to_datetime(tests_malaysia_df.date)
hospital_df.index = pd.to_datetime(hospital_df.date)
icu_df.index = pd.to_datetime(icu_df.date)
checkin_malaysia_df.index = pd.to_datetime(checkin_malaysia_df.date)
trace_malaysia_df.index = pd.to_datetime(trace_malaysia_df.date)

# Drop Date Columns
hospital_df.drop(columns='date', inplace=True)
icu_df.drop(columns='date', inplace=True)

# Transform
# Combine Number of PCR and Antigen Rapid Test Kits
tests_malaysia_df['total_test'] = tests_malaysia_df['rtk-ag'] + tests_malaysia_df['pcr']

# Sum up Covid Admission of all states
hospital_df['total_beds_available'] = hospital_df['beds'] + hospital_df['beds_noncrit']
hospital_covid_df = hospital_df.groupby('date')[['total_beds_available','admitted_covid', 'discharged_covid', 'hosp_covid']].sum()

# Sum up ICU Status of all states
icu_covid_df = icu_df.groupby('date')[['bed_icu_covid', 'icu_covid', 'vent_covid']].sum()

# Merge Datasets
malaysia_daily_stats_df = cases_malaysia_df[['cases_new']]\
                .merge(deaths_malaysia_df['deaths_new'], on='date')\
                .merge(tests_malaysia_df['total_test'], on='date')\
                .merge(checkin_malaysia_df[['checkins', 'unique_ind', 'unique_loc']], on='date')\
                .merge(trace_malaysia_df['casual_contacts'], on='date')\
                .merge(hospital_covid_df, on='date')\
                .merge(icu_covid_df, on='date')

# Export CSV
malaysia_daily_stats_df.to_csv("malaysia_covid_daily_stats.csv")
print("Updated Successfully Until : {}".format(malaysia_daily_stats_df.index[-1]))

