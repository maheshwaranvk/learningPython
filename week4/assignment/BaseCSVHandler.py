import pandas as pd

class BaseCSVHandler:
    props = {}
    def readCSVFile(self, fileName):
        csvFileRawData = pd.read_csv(f"{fileName}")
        return csvFileRawData
    
    def writeCSVFile(self, dataDF, fileName, indexValue):
        dataDF.to_csv(f"{fileName}", index=indexValue)

    def readPropertyFile(self):
        with open("config.properties",'r') as f:
            for line in f:
                if line and not line.startswith("#"):
                    key,value=line.split(":",1)
                    self.props[key.strip()] = value.strip()
            return self.props