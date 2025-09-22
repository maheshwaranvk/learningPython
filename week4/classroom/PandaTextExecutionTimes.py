import pandas as pd

testExecutionTimes = pd.Series([12,15,20,18,25,30,22], index=['TC1','TC2','TC3','TC4','TC5','TC6','TC7'])
print(testExecutionTimes)

print(testExecutionTimes[:3])
print(testExecutionTimes.mean())
print(testExecutionTimes.iloc[1])
print(testExecutionTimes.loc['TC3'])