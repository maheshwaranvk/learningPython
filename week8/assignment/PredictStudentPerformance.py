import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import logging

rawData = pd.read_csv('Student_Performance.csv')

class StudentPerformanceModel:

    def __init__(self):
        self.scallingRequired = False
        self.cleanedData = pd.DataFrame()
        self.scaler = None
        self.model = LinearRegression()

    def findCorrelation(self):
        correlation_with_closure = rawData.corr(numeric_only=True)[['Performance Index']].drop(index='Performance Index')
        sns.heatmap(correlation_with_closure, annot=True, fmt=".2g", cmap='viridis', cbar=True)
        plt.title('Correlation Heatmap')
        plt.show()
    
    def handlingMissingData(self):
        #getting the col names which have null value
        nullValueColumnNames = rawData.columns[rawData.isnull().any()]
        print(nullValueColumnNames)
        #checking its skew
        print(rawData[nullValueColumnNames].skew())
        print("Null count -> " , rawData.isnull().sum())
        for columns in nullValueColumnNames:
            if (rawData[columns].skew()>-0.5 and rawData[columns].skew()<0.5):
                print(f"updating the {columns} null value with mean value")
                rawData[columns].fillna(round(rawData[columns].mean(), 2),inplace=True)
            else:
                print(f"updating the {columns} null value with median value")
                rawData[columns].fillna(round(rawData[columns].median(), 2),inplace=True)
        print("Null count -> " , rawData.isnull().sum())

    def isScallingRequired(self):
        summary = rawData.describe().T[['min', 'max']]
        summary['range'] = summary['max'] - summary['min']
        print(summary.sort_values(by='range', ascending=False))
        #getting only the columns having number
        columnsHavingnums = rawData.select_dtypes(include=['int64','float64']).columns
        #finding the range
        range = rawData[columnsHavingnums].max() - rawData[columnsHavingnums].min()
        rangeRatio = range.max() / (range.min() + 1e-9)
        self.scallingRequired = rangeRatio > 10
        return self.scallingRequired
    
    def calculateOutlier(self):
        columnsHavingnums = rawData.select_dtypes(include=['int64','float64']).columns
        for column in columnsHavingnums:
            Q1 = rawData[column].quantile(0.25)
            Q3 = rawData[column].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            outliers = rawData[(rawData[column] < lower) | (rawData[column] > upper)]
            logging.debug(f"outliers for {column} is {outliers}")
            filteredData = rawData[(rawData[column] >= lower) & (rawData[column] <= upper)]
            self.cleanedData[column] = filteredData[column]
            #print(self.cleanedData)
    
    def scallingData(self, inputData, fit=True):
        columnsHavingnums = inputData.select_dtypes(include=['int64','float64']).columns
        overallSkew = inputData[columnsHavingnums].skew().abs().mean()
        if overallSkew <= 0.5:
            scaler = StandardScaler()
        else:
            scaler = RobustScaler()
        
        if fit or self.scaler is None:
            scaledData = pd.DataFrame(scaler.fit_transform(inputData), columns=inputData.columns, index=inputData.index)
            self.scaler=scaler
        else:
            scaledData = pd.DataFrame(self.scaler.transform(inputData), columns=inputData.columns, index=inputData.index)
        return scaledData

    def multiLinearRegression(self, scaledData1, featureList, label):
        x = scaledData1[featureList]
        y = scaledData1[label]
        xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2, random_state=10)
        self.model.fit(xtrain,ytrain)
        ypredit = self.model.predict(xtest)
        print("Bo : ", self.model.intercept_)
        print("Co Efficients", self.model.coef_)
        print(f"{self.model.intercept_} + {self.model.coef_[0]}*X1 + {self.model.coef_[1]}*X2 + {self.model.coef_[2]}*X3 + {self.model.coef_[3]}*X4")
        print("Evaluation Metrics")
        print("MSE : ",mean_squared_error(ytest,ypredit))
        print("RMSE : ",root_mean_squared_error(ytest,ypredit))
        print("R Square : ",r2_score(ytest,ypredit))
        plt.scatter(ytest, ypredit)
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title("Actual vs Predicted")
        plt.show()
    
    def predictPerformance(self, hoursStudied, PreviousScore, sleepHours, sampleQuesPaperPracticed):
        x_user = pd.DataFrame(
        [[hoursStudied, PreviousScore, sleepHours, sampleQuesPaperPracticed]],
        columns=["Hours Studied", "Previous Scores", "Sleep Hours", "Sample Question Papers Practiced"]
        )
        xUserScaled = self.scallingData(x_user, fit=False)
        final = self.model.predict(xUserScaled)
        print("Predicted Performance Index :", int(final[0]))
    
if __name__=="__main__":
    obj = StudentPerformanceModel()
    obj.findCorrelation()
    obj.handlingMissingData()
    print(obj.scallingRequired)
    obj.isScallingRequired()
    print(obj.scallingRequired)
    if (obj.scallingRequired):
        obj.calculateOutlier()
    else:
        obj.cleanedData = rawData
    # scaled_data = obj.scallingData(obj.cleanedData.drop(columns=["Performance Index"]), fit=True)
    # obj.multiLinearRegression(scaled_data, ["Hours Studied", "Previous Scores", "Sleep Hours", "Sample Question Papers Practiced"],"Performance Index")
    X = obj.cleanedData.drop(columns=["Performance Index"])
    y = obj.cleanedData["Performance Index"]
    scaled_X = obj.scallingData(X, fit=True)
    scaled_data = scaled_X.copy()
    scaled_data["Performance Index"] = y.values
    obj.multiLinearRegression(scaled_data, ["Hours Studied", "Previous Scores", "Sleep Hours", "Sample Question Papers Practiced"], "Performance Index")
    obj.predictPerformance(8,99,4,9)