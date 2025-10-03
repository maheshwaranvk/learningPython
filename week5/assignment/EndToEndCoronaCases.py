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
#print(DeathCasesDF['Deaths'].idxmin(), ":", DeathCasesDF['Deaths'].min())

#print(rawCSVData[rawCSVData['Country/Region']=='India'])

ConfirmedCasesDF = pd.DataFrame(ConfirmedCases)
#print([pd.DataFrame(DeathCasesDF),pd.DataFrame(ConfirmedCasesDF)])
CFR = pd.DataFrame((DeathCasesDF['Deaths']/ConfirmedCasesDF['Confirmed'])*100)
CFR=CFR.rename(columns={0:"CFR"})
CFR.to_csv("CFR_Region.csv")

#print(pd.DataFrame(RecoveredCases))

groupByCountryAndRegion = rawCSVData.groupby(['WHO Region','Country/Region']).sum()
groupByCountryAndRegion.to_csv("CountryRegionGrouped.csv")

recoveredCasesGroup = rawCSVData.groupby('Recovered').sum()
recoveredCasesGroupDF = pd.DataFrame(recoveredCasesGroup.reset_index())
#rawCSVData[rawCSVData['Recovered']==0].reset_index(drop=True).to_csv("ReceoveredRates.csv")

#print(rawCSVData['Active'].mean())
#print(rawCSVData['Active'].std())

startingOutliner = rawCSVData['Active'].mean()
endingOutliner = 2*rawCSVData['Active'].std()
lowerBound = startingOutliner-endingOutliner
upperBound = startingOutliner+endingOutliner

rawCSVData[(rawCSVData['Active']>lowerBound) & (rawCSVData['Active']<upperBound)].to_csv("ActiveOutliners.csv")