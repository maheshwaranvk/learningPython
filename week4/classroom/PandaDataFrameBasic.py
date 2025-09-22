import pandas as pd
import numpy as np

#using list
array1 = [10,20,30]
array2 = [30,40,50]

data1 = np.array(array1)
data2 = np.array(array2)

df1 = pd.DataFrame([array1,array2], columns=['A','B','C'])
print(df1)

#using series
series1 = pd.Series([100,200,300], index=['A','B','C'])
series2 = pd.Series([400,500], index=['A','B'])
df2 = pd.DataFrame([series1,series2])
print(df2)

#using Dictionary of Series
markSheet = {'Mani': pd.Series([10,20,30]),
             'Alex': pd.Series([20,30])}
print(pd.DataFrame(markSheet))