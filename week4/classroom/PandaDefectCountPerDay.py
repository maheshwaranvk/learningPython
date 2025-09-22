import pandas as pd

defectLogged=pd.Series([5,8,3,6,10,2,7], index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])

print(defectLogged)
print(defectLogged.max())
print(defectLogged.idxmin())
print(defectLogged.iloc[4])
print(defectLogged.loc['Wed'])
print(defectLogged.sum())