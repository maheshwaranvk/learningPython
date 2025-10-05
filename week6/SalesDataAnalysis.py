import pandas as pd

rawData = pd.read_csv("SalesDataset.csv")
print("25th percentile of Total Amount : ", rawData['Total Amount'].quantile(0.25))
print("50th percentile of Total Amount : ", rawData['Total Amount'].quantile(0.50))
print("75th percentile of Total Amount : ", rawData['Total Amount'].quantile(0.75))
totalAmountDescribe = rawData['Total Amount'].describe()
print(totalAmountDescribe)

print("Variance in Total Amount : ", rawData['Total Amount'].var())
print("Variance in Quantity : ", rawData['Quantity'].var())

# print(rawData[['Age','Total Amount']].corr())
# print(rawData[['Quantity','Total Amount']].corr())
# print(rawData[['Price per Unit','Total Amount']].corr())

print(rawData[['Age','Total Amount','Quantity','Price per Unit']].corr())