import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data_dict = {
    'x1': [1, 2, 3],
    'x2': [2, 1, 4],
    'Output': [6, 8, 14]
}
data = pd.DataFrame(data_dict)

x = data[['x1','x2']]
y = data['Output']

xtest = x
xtrain = x
ytest = y
ytrain = y

model = LinearRegression()
model.fit(xtrain,ytrain)

print ("Intercept : ", model.intercept_)
print ("Co efficient : ", model.coef_)
print(f"Model Equation: y = {model.intercept_:.1f} + {model.coef_[0]:.1f}*x1 + {model.coef_[1]:.1f}*x2\n")

ypred = model.predict(xtest)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xtest['x1'], xtest['x2'], ytest, color='blue', s=100, label='Actual Data Points')

x1_surf = np.linspace(x['x1'].min(), x['x1'].max(), 10)  # creates 10 linear points from min to max
x2_surf = np.linspace(x['x2'].min(), x['x2'].max(), 10)
x1_surf, x2_surf = np.meshgrid(x1_surf, x2_surf)

y_plane = model.predict(pd.DataFrame({'x1': x1_surf.ravel(), 'x2': x2_surf.ravel()}))
y_plane = y_plane.reshape(x1_surf.shape)

ax.plot_surface(x1_surf, x2_surf, y_plane, color='red', alpha=0.3, label='Predicted Plane')
#ax.set_xlabel('x1 (Total Years of Experience - equivalent)')
#ax.set_ylabel('x2 (Rating)')
#ax.set_zlabel('Salary')
#ax.set_title('Salary Prediction (3D Regression Plane)')
ax.legend()

plt.show()