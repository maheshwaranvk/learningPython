import pandas as pd

rawData = pd.read_csv('SalesDataset(1).csv')

percentile25 = rawData['Total Amount'].quantile(0.25)
percentile75 = rawData['Total Amount'].quantile(0.75)

IQR = percentile75 - percentile25

lowerBound = percentile25 - (1.5 * IQR)
outerBound = percentile75 + (1.5 * IQR)

outlier = rawData[(rawData['Total Amount']<lowerBound) | (rawData['Total Amount']>outerBound)]

outlier.to_csv('Outlier_SalesDataSet.csv')

cleanedDataWithoutOutliers = rawData.drop(outlier.index)

print(cleanedDataWithoutOutliers)
cleanedDataWithoutOutliers.to_csv('SalesDataSet_WithoutOutlier.csv')