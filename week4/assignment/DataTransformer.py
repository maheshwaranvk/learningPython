from week4.assignment.BaseCSVHandler import BaseCSVHandler
import pandas as pd

class DataTransformer(BaseCSVHandler):
    props = {}
    def __init__(self):
        super().__init__()

    def readPropertyFile(self):
        with open("config.properties",'r') as f:
            for line in f:
                if line and not line.startswith("#"):
                    key,value=line.split(":",1)
                    self.props[key.strip()] = value.strip()
            return self.props

    def getRowDetails(self, rowIndex):
        readCsvData = self.readCSVFile(self.readPropertyFile()['csvFileLocation'])
        rowDetails = readCsvData.loc[rowIndex]
        print(rowDetails)

    def getColumnDetails(self):
        readCsvData = self.readCSVFile(self.readPropertyFile()['csvFileLocation'])
        columnDetails = readCsvData.columns
        print(pd.Series(columnDetails))

    def groupByFilters(self, groupByValue, method):
        readCsvData = self.readCSVFile(self.readPropertyFile()['csvFileLocation'])
        match method.lower():
            case "sum":
                return readCsvData.groupby(groupByValue).sum()
            case "mean":
                return readCsvData.groupby(groupByValue).mean(numeric_only=True)
            case "max":
                return readCsvData.groupby(groupByValue).max(numeric_only=True)
            case "min":
                return readCsvData.groupby(groupByValue).min(numeric_only=True)
            case "count":
                return readCsvData.groupby(groupByValue).count()
            case "size":
                return readCsvData.groupby(groupByValue).size()
            case "agg":
                return readCsvData.groupby(groupByValue).agg(["mean", "sum", "count"])
            case _:
                raise ValueError(f"Unsupported aggregation method: {method}")

if __name__=="__main__":
    p1 = DataAnalyser()
    print(p1.groupByFilters("WHO Region","size"))
