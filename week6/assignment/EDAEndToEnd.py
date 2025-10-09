import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

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

outliersConfirmedCases = rawCSVData[(rawCSVData['Confirmed']<confirmedLowerBound) | (rawCSVData['Confirmed']>confirmedUpperBound)]
outliersNewCases = rawCSVData[(rawCSVData['New cases']<newCasesLowerBound) | (rawCSVData['New cases']>newCasesUpperBound)]

outlierIndex = outliersConfirmedCases.index.union(outliersNewCases.index)
cleanestData = rawCSVData.drop(outlierIndex)

print(cleanestData)

#4
stdScalar = StandardScaler()
stdCleanedData = stdScalar.fit_transform(rawCSVData[['Confirmed','New cases']])
print(stdCleanedData)

stdCleaned_df = pd.DataFrame(stdCleanedData, columns=['Confirmed_scaled', 'New_cases_scaled'])
print(stdCleaned_df)

#5.2
correlation = confirmedCases[['Confirmed','New cases']].corr()
#sns.heatmap(correlation, annot=True, fmt=".0f", cmap='viridis', cbar=True)
#plt.title('Correlation Heatmap')
#plt.show()

#5.1
#stdCleaned_df['Confirmed_scaled'].to_csv('ConfirmedScaled.csv')
print(rawCSVData['Confirmed'])

# df = pd.DataFrame({
#     'beforeScalarConfirmed' : rawCSVData['Confirmed'],
#     'afterScalarConfirmed' : stdCleaned_df['Confirmed_scaled']
# })
# print(df)

plt.figure(figsize=(10,6))
sns.histplot(stdCleaned_df['Confirmed_scaled'], color='green', kde=True, stat='density')
#sns.histplot(rawCSVData['Confirmed'], color='red', kde=True, stat='density')
plt.xlim(-0.7, 0.7)
plt.title("Bell Curve Visualization with Histogram and KDE")
plt.show()