import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

#1
rawData = pd.read_csv('house_price_regression_dataset.csv')
modelingData = rawData[["Square_Footage", "House_Price"]].copy()

#2
print(modelingData)
modelingData['House_Price'] = modelingData['House_Price'].fillna(modelingData['House_Price'].mean())
modelingData['Square_Footage'] = modelingData['Square_Footage'].fillna(modelingData['Square_Footage'].mean())
plt.scatter(modelingData['Square_Footage'], modelingData['House_Price'], marker='o', color='green', label='House Price Range')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.legend()
plt.show()

#3
x = modelingData[['Square_Footage']]
y = modelingData['House_Price']

#4
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=10)

#5
model = LinearRegression()
model.fit(xtrain, ytrain)

ypredit = model.predict(xtest)

plt.scatter(xtest, ytest, marker='o', color = 'red', label='Testing Values', alpha=0.3)
plt.plot(xtest, ypredit, color='blue', label = 'Predicted Values')

plt.xlabel("Square Footage")
plt.ylabel("House Price")
plt.legend()
plt.show()

print("MSE : ", mean_squared_error(ytest, ypredit))
print("RMSE : ", np.sqrt(mean_squared_error(ytest, ypredit)))
print("R Square : ", r2_score(ytest, ypredit))
