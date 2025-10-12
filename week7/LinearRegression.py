import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

rawData = pd.read_csv('salary.csv')

x = rawData[['YearsExperience']]
y = rawData['Salary']

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=10)

model = LinearRegression()
model.fit(xtrain, ytrain)

ypredit = model.predict(xtest)

#evaluation of predicted values with test values
print("MSE : ", mean_squared_error(ytest, ypredit))
print("R Square : ", r2_score(ytest, ypredit))

plt.scatter(xtest, ytest, color='red', label="Actual Test Values")
plt.plot(xtest, ypredit, color='green', label="Predicted Values")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()