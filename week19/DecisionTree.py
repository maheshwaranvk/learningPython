import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv(r"decisiontree.csv")


df = df.dropna()

le_dict = {}

for column in df.columns:
    if df[column].dtype in ['object', 'str']:
        le = LabelEncoder()
        encoded_values = le.fit_transform(df[column])
        df[column] = encoded_values  # directly assign numpy array
        le_dict[column] = le  # store encoders for future use


X = df.drop(['Day', 'Play'], axis=1)   # features
y = df['Play']                         # target

# Save column names before converting to numpy
feature_names = X.columns.tolist()

# Convert to numpy arrays to ensure numeric types
X = np.array(X)
y = np.array(y)

model = DecisionTreeClassifier(criterion="entropy", max_depth=3)
model.fit(X, y)


plt.figure(figsize=(20, 12))   
plot_tree(
    model,
    feature_names=feature_names,
    class_names=le_dict['Play'].classes_,
    filled=True,
    fontsize=12
)
plt.show()


def predict_play(weather, temperature, humidity, wind):
   
    w = le_dict['Weather'].transform([weather])[0]
    t = le_dict['Temperature'].transform([temperature])[0]
    h = le_dict['Humidity'].transform([humidity])[0]
    wi = le_dict['Wind'].transform([wind])[0]


    user_input = pd.DataFrame([[w, t, h, wi]], columns=feature_names)

 
    prediction = model.predict(np.array(user_input))[0]


    return le_dict['Play'].inverse_transform([prediction])[0]


print(predict_play("Sunny", "Cool", "Normal", "Weak"))   # Expected output: Yes
print(predict_play("Rain", "Mild", "High", "Strong"))    # Expected output: No
