import pandas as pd
import matplotlib.pyplot as plt

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
