from week4.assignment.BaseCSVHandler import BaseCSVHandler
import pandas as pd

class DataCleaner(BaseCSVHandler):
    
    def __init__(self):
        super().__init__()
        self.cleanedData = pd.DataFrame(self.readCSVFile(self.readPropertyFile()['csvFileLocation']))

#updating column header to be with specific format : First letter UpperCase and rest are lower case
    def updateColumnHeaderFormat(self):
        updatedColumnData=[]
        for column in self.cleanedData.columns.to_list():
            updatedColumnData.append(column.capitalize())
        self.cleanedData.columns = updatedColumnData
    
#remove duplicate rows in the csv file
    def removeDuplicateRows(self):
        self.cleanedData = self.cleanedData.drop_duplicates().reset_index(drop=True)

#create a new clean csv file
    def createCleanDataSet(self, fileName):
        self.writeCSVFile(self.cleanedData, fileName, False)