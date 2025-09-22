import pandas as py

data = {"DefectId":['D1','D2','D3','D4','D5'],
        "Module":['Login','Payment','Reports','Login','Payment'],
        "Severity":['High','Medium','Low','High','Medium'],
        "Status":['Open','Closed','Open','Closed','Open']                             
        }

dataDf = py.DataFrame(data)
print(dataDf)
print(dataDf[dataDf["Status"]=='Open'])
print(dataDf.groupby("Status")['Module'].count())
groupSeverity = dataDf.groupby('Severity')
print(groupSeverity.get_group("High"))

dataStatus=dataDf.groupby("Status")["DefectId"].count()
print(dataStatus)