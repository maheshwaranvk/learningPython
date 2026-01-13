import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,5,4,5])
xtest = np.array([6,7,8,9,10]).reshape(-1,1)

model = LinearRegression()

model.fit(x,y)
yPredict = model.predict(xtest)

print(yPredict)

plt.scatter(x,y,color='b',label="Linear")
plt.plot(xtest,yPredict,color='r',label="Linear")
plt.show()