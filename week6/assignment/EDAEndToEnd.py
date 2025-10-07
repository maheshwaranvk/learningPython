import pandas as pd

rawCSVData = pd.read_csv("country_wise_latest.csv")

#1
confirmedCases = rawCSVData[['country/Region','Confirmed','New cases']]

#2
print(f" Mean for Confirmed: {confirmedCases['Confirmed'].mean()} & New Cases : {confirmedCases['New cases'].mean()}")
print(f" Median for Confirmed: {confirmedCases['Confirmed'].median()} & New Cases : {confirmedCases['New cases'].median()}")
print(f" Standard Deviation for Confirmed: {confirmedCases['Confirmed'].std()} & New Cases : {confirmedCases['New cases'].std()}")
print(f" Variance for Confirmed: {confirmedCases['Confirmed'].var()} & New Cases : {confirmedCases['New cases'].var()}")
print(confirmedCases[['Confirmed','New cases']].corr())

#3
cperc25 = rawCSVData['Confirmed'].quantile(0.25)
cperc75 = rawCSVData['Confirmed'].quantile(0.75)

IQR = cperc75 - cperc25

confirmedLowerBound = cperc25 - (1.5* IQR)
confirmedUpperBound = cperc75 + (1.5* IQR)
print(confirmedLowerBound)
print(confirmedUpperBound)

nperc25 = confirmedCases['New cases'].quantile(0.25)
nperc75 = confirmedCases['New cases'].quantile(0.75)

IQR1 = nperc75 - nperc25

newCasesLowerBound = nperc25 - (1.5* IQR1)
newCasesUpperBound = nperc75 + (1.5* IQR1)

print(newCasesLowerBound)
print(newCasesUpperBound)
print(rawCSVData[(rawCSVData['Confirmed']<confirmedLowerBound) | (rawCSVData['Confirmed']>confirmedUpperBound)])
print(rawCSVData[(rawCSVData['New cases']<newCasesLowerBound) | (rawCSVData['New cases']>newCasesUpperBound)])