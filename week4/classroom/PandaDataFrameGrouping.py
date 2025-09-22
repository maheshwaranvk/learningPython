import pandas as pd

data = {
    "TestCase": ["TC1", "TC2", "TC3", "TC4", "TC5" , "TC6"],
    "Module": ["Login", "Login", "Payment", "Payment", "Reports", "Reports"],
    "Status": ["Passed", "Failed", "Passed", "Failed", "Passed", "Passed"],
    "Duration": [12, 15, 20, 18, 25, 22]
}

dataDf = pd.DataFrame(data)
print(dataDf.groupby("Status")["TestCase"].count())
print(dataDf.groupby("Module")["Duration"].mean())