import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error
import matplotlib.pyplot as plt


rawData = pd.read_csv('salary_2610.csv')
x = rawData[['YearsExperience','Rating']]
y = rawData['Salary']

xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2, random_state=10)

model = LinearRegression()
model.fit(xtrain,ytrain)

ypredit = model.predict(xtest)

print("Bo : ", model.intercept_)
print("Co ef of B1 & B2 : ", model.coef_)
#Y= Bo + B1X1 + B2X2
print(f"{model.intercept_} + {model.coef_[0]}*X1 + {model.coef_[1]}*X2")

print("Evaluation Metrics")
print("MSE : ",mean_squared_error(ytest,ypredit))
print("RMSE : ",root_mean_squared_error(ytest,ypredit))
print("R Square : ",r2_score(ytest,ypredit))

yoe = int(input("Enter the Years of Experience : "))
rating = int(input("Enter the Rating : "))

# new_data = pd.DataFrame({
#     "Years of Experience" : yoe,
#     "Rating" : rating
# })

# print(model.predict(new_data))

x_user = pd.DataFrame([[yoe,rating]])

final = model.predict(x_user)
print("Predicted Salary : $", final[0])