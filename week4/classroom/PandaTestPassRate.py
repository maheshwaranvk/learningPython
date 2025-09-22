import pandas as pd

testPassRate = pd.Series([80,85,78,90,88], index=['B1','B2','B3','B4','B5'])

print(testPassRate)
print(testPassRate.mean())
print(testPassRate.idxmax())
print(testPassRate.iloc[-1])
print(testPassRate.loc['B3'])
print(testPassRate - testPassRate.mean())