from sklearn.preprocessing import StandardScaler
import numpy as np

stdScaler = StandardScaler()

rawData = np.array([[1,2],[3,4],[5,6]])

print ("Fit Data", stdScaler.fit(rawData))
print ("Transform Data", stdScaler.transform(rawData))

transformedData = stdScaler.fit_transform(rawData)
print(transformedData)