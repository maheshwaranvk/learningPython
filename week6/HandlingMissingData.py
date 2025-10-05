import pandas as pd

rawData = pd.read_csv('tests_results_missing.csv')
print("number of missing values : ", rawData.isnull().sum())
meanDuation = rawData['Duration'].mean()
rawData['Duration'] = rawData['Duration'].fillna(meanDuation)
rawData['Status'] = rawData['Status'].fillna("Unknown")
rawData = rawData.dropna()

print(rawData)