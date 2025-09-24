import pandas as pd

class BaseCSVHandler:

    def readCSVFile(self, fileName):
        csvFileRawData = pd.read_csv(f"{fileName}")
        return csvFileRawData
    
    def writeCSVFile(self, dataDF, fileName):
        dataDF.to_csv(f"{fileName}", index=False)

# if __name__ == "__main__":
#     p1 = BaseCSVHandler()
#     data = p1.readCSVFile("S:/AI TL/VS Projects/learningPython/week4/assignment/country_wise_latest.csv")
#     writeData = data.head()
#     p1.writeCSVFile(writeData, "firstFive.csv")