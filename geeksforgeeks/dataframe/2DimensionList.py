#https://www.geeksforgeeks.org/python/make-a-pandas-dataframe-with-two-dimensional-list-python/

#using 2D array
import pandas as pd
data = [['Mahesh',10],
        ['Siva',20],
        ['Aruvi',30]]
print(data)
dataDf = pd.DataFrame(data,columns=['Name','TestCaseCount'])
print(dataDf)

#using dictionary
dataD = {'Mahesh':10,
         'Siva':20,
         'Aruvi':30}
print(dataD)
dataDfD = pd.DataFrame(list(dataD.items()),columns=['Name','TestCaseCount'])
print(dataDfD)

#using Series
dataSeries = pd.Series(['Mahesh',10],index=['Name','TestCaseCount'])
dataSeries2 = pd.Series(['Siva',20],index=['Name','TestCaseCount'])
dataSeries3 = pd.Series(['Aruvi',30],index=['Name','TestCaseCount'])

dataSeriesDF = pd.DataFrame([dataSeries,dataSeries2,dataSeries3])
print(dataSeriesDF)