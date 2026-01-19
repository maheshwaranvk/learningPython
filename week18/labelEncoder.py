import numpy as np
from sklearn.preprocessing  import LabelEncoder

le = LabelEncoder()
le.fit(["Red","Blue","Green","Yellow", "Yellow", "yellow"])
print(le.transform(["Red","Blue","Green","Yellow"]))
print(le.inverse_transform([0,1,2,3,4]))