import pandas as pd

data = {"TestCase":['TC1','TC2','TC3','TC4','TC5'],
        "Status":['Passed','Failed','Passed','Failed','Passed'],
        "Duration":[12,15,20,18,20]
        }
dataDF = pd.DataFrame(data)
print(dataDF)
print(dataDF['Status'])
print(dataDF[dataDF["Status"]=='Failed'])
dataDF.to_csv("test.csv",index=False)
readCSV = pd.read_csv('test.csv')
print(readCSV)