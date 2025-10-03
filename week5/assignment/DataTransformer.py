from week5.assignment.DataCleaner import DataCleaner
import pandas as pd

class DataTransformer(DataCleaner):
    def __init__(self):
        super().__init__()
    
    def getRawData(self):
        rawCsvData = self.readCSVFile(self.readPropertyFile()['cleanedDataSet'])
        return rawCsvData

    def getRowDetails(self, rowIndex):
        readCsvData = self.readCSVFile(self.readPropertyFile()['cleanedDataSet'])
        rowDetails = readCsvData.loc[rowIndex]
        print(rowDetails)

    def getColumnDetails(self):
        readCsvData = self.readCSVFile(self.readPropertyFile()['cleanedDataSet'])
        columnDetails = readCsvData.columns
        print(pd.Series(columnDetails))

    def groupByFiltersAndColumn(self, groupByValue, columnName, method):
        readCsvData = self.readCSVFile(self.readPropertyFile()['cleanedDataSet'])
        match method.lower():
            case "sum":
                return readCsvData.groupby(groupByValue)[columnName].sum()
            case "mean":
                return readCsvData.groupby(groupByValue)[columnName].mean()
            case "max":
                return readCsvData.groupby(groupByValue)[columnName].max()
            case "min":
                return readCsvData.groupby(groupByValue)[columnName].min()
            case "count":
                return readCsvData.groupby(groupByValue)[columnName].count()
            case "size":
                return readCsvData.groupby(groupByValue)[columnName].size()
            case "agg":
                return readCsvData.groupby(groupByValue)[columnName].agg(["mean", "sum", "count"])
            case _:
                raise ValueError(f"Unsupported aggregation method: {method}")
            
    def groupByFilters(self, groupByValue, method):
        readCsvData = self.readCSVFile(self.readPropertyFile()['cleanedDataSet'])
        match method.lower():
            case "sum":
                return readCsvData.groupby(groupByValue).sum()
            case "mean":
                return readCsvData.groupby(groupByValue).mean()
            case "max":
                return readCsvData.groupby(groupByValue).max()
            case "min":
                return readCsvData.groupby(groupByValue).min()
            case "count":
                return readCsvData.groupby(groupByValue).count()
            case "size":
                return readCsvData.groupby(groupByValue).size()
            case "agg":
                return readCsvData.groupby(groupByValue).agg(["mean", "sum", "count"])
            case _:
                raise ValueError(f"Unsupported aggregation method: {method}")
