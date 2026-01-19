import numpy as np
from sklearn.linear_model import Ridge

X = np.array([ [1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 2])

model = Ridge(alpha=1.0, fit_intercept=False)

model.fit(X,y)

print(model.coef_)