import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error

rawData = pd.read_csv("multiLinearRegression.csv")

X = rawData[["Test_Steps","Avg_Page_Load_Time"]]
Y = rawData["Execution_Time"]

xTrain, xTest, yTrain, yTest = train_test_split(X,Y,test_size=0.2,random_state=10)

model = LinearRegression()
model.fit(xTrain,yTrain)

yPredit = model.predict(xTest)

print("Bo : ", model.intercept_)
print("Co ef of B1 & B2 : ", model.coef_)
#Y= Bo + B1X1 + B2X2
print(f"{model.intercept_} + {model.coef_[0]}*X1 + {model.coef_[1]}*X2")

print("Evaluation Metrics")
print("MSE : ",mean_squared_error(yTest,yPredit))
print("RMSE : ",root_mean_squared_error(yTest,yPredit))
print("R Square : ",r2_score(yTest,yPredit))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xTest['Test_Steps'], xTest['Avg_Page_Load_Time'], yTest, color='blue', s=100, label='Actual Data Points')

x1_surf = np.linspace(X['Test_Steps'].min(), X['Test_Steps'].max(), 10)  # creates 10 linear points from min to max
x2_surf = np.linspace(X['Avg_Page_Load_Time'].min(), X['Avg_Page_Load_Time'].max(), 10)
x1_surf, x2_surf = np.meshgrid(x1_surf, x2_surf)

y_plane = model.predict(pd.DataFrame({'Test_Steps': x1_surf.ravel(), 'Avg_Page_Load_Time': x2_surf.ravel()}))
y_plane = y_plane.reshape(x1_surf.shape)

ax.plot_surface(x1_surf, x2_surf, y_plane, color='red', alpha=0.3, label='Predicted Plane')

# Add axis labels
ax.set_xlabel('Test Steps', fontsize=12, fontweight='bold')
ax.set_ylabel('Avg Page Load Time', fontsize=12, fontweight='bold')
ax.set_zlabel('Execution Time', fontsize=12, fontweight='bold')
ax.set_title('3D Linear Regression: Execution Time Prediction', fontsize=14, fontweight='bold', pad=20)

# Add legend
ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()

print("\n" + "="*50)
print("Prediction for New Data")
print("="*50)

test_steps = float(input("Enter Test Steps: "))
avg_page_load_time = float(input("Enter Average Page Load Time: "))

user_input = pd.DataFrame({'Test_Steps': [test_steps], 'Avg_Page_Load_Time': [avg_page_load_time]})

predicted_execution_time = model.predict(user_input)[0]

print(f"\nFor Test_Steps = {test_steps} and Avg_Page_Load_Time = {avg_page_load_time}")
print(f"Predicted Execution Time: {predicted_execution_time:.2f}")
