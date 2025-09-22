#https://www.geeksforgeeks.org/python/python-creating-dataframe-from-dict-of-narray-lists/

import pandas as pd

#Dictionary of list
data = {
    'Name':['Mahesh','Dinesh','Mala'],
    'Age':[33,32,33],
    'YOE':[13,8,10]
}
dataDF = pd.DataFrame(data)
print(dataDF)

#Dictionary of Series

dataD = {
    'Mahesh': pd.Series([10,20,30], index=['TC1','TC2','TC3']),
    'Siva': pd.Series([40,50,60], index=['TC1','TC2','TC3'])
}

print(pd.DataFrame(dataD))