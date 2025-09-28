import pandas as pd

df = pd.read_csv('variant.csv')
print(df)

#Univariate Analysis
print(df['Duration'].mean())
print(df['Duration'].std())
print(df['Duration'].median())

#Bivariate Analysis
print(df.groupby('Status')['Duration'].mean())

#Multivariate Analysis
print(df.groupby(["Module","Status"])['Defects'].sum())