import pandas as pd

rawCSVData = pd.read_csv("country_wise_latest.csv")


ConfirmedCases = rawCSVData.groupby('WHO Region')['Confirmed'].sum()
DeathCases = rawCSVData.groupby('WHO Region')['Deaths'].sum()
RecoveredCases = rawCSVData.groupby('WHO Region')['Recovered'].sum()

req1=pd.DataFrame([ConfirmedCases,DeathCases,RecoveredCases])
#req1.transpose().to_csv("ConfirmedDeathRecoveredCases.csv")

countryWiseConfirmedCase = rawCSVData.groupby('Country/Region')['Confirmed'].sum()
req2 = pd.DataFrame(countryWiseConfirmedCase)
#req2[req2['Confirmed']>10].to_csv("FilteredLowCaseRecords.csv")

maxConfirmedCase = rawCSVData.groupby('WHO Region')['Confirmed'].max()
req3 = pd.DataFrame(maxConfirmedCase)
#print(req3['Confirmed'].idxmax(), ":", req3['Confirmed'].max())

confirmedCoronaCases = pd.DataFrame(rawCSVData.groupby('Confirmed').sum())
req4=confirmedCoronaCases.sort_values('Confirmed')
#req4.to_csv("SortedCoronaCases.csv")

NewCoronaCases = pd.DataFrame(rawCSVData.groupby('New cases').sum())
(NewCoronaCases.sort_values('New cases', ascending=False)).head().to_csv("Top5NewCases.csv")

DeathCasesDF = pd.DataFrame(DeathCases)
