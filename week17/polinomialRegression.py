import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

X = np.array([1,2,3,4]).reshape(-1,1)
Y = np.array([1,4,9,15])

poly = PolynomialFeatures(degree=2)

xPoly = poly.fit_transform(X)

model = LinearRegression()
model.fit(xPoly,Y)

yPredit = model.predict(xPoly)

plt.scatter(X,Y,color='blue',label='Actual')
plt.plot(X, yPredit,color='red',label='Predicted')
plt.legend()
plt.show()