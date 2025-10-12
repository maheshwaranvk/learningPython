import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

data = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])

scalar = MinMaxScaler()
minMaxScaledData = scalar.fit_transform(data)
print(minMaxScaledData)

scalar2 = RobustScaler()
robustScaledData = scalar2.fit_transform(data)
#print(robustScaledData)