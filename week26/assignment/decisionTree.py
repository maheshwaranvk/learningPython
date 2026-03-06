import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.tree import plot_tree

raw_data = pd.read_csv("customer_purchase_data.csv")

print(raw_data.head())
X = raw_data[['Age','EstimatedSalary']]
y=raw_data['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_predit = model.predict(X_test)

cm = confusion_matrix(y_test, y_predit)
acc = accuracy_score(y_test, y_predit)
prec = precision_score(y_test, y_predit)
rec = recall_score(y_test, y_predit)

print("Confusion matrix:\n", cm)
print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", rec)

plt.figure(figsize=(12, 6))
plot_tree(
    model,
    feature_names=["Age", "EstimatedSalary"],
    class_names=["Not Purchased", "Purchased"],
    filled=True
)
plt.show()
age = int(input("Enter the age: "))
estimated_salary = int(input("Enter the estimated salary: "))

user_x = pd.DataFrame([[age, estimated_salary]],
                      columns=['Age', 'EstimatedSalary'])
pred = model.predict(user_x)[0]
print("Prediction (0=Not Purchased, 1=Purchased):", pred)
print ("Not Purcharsed" if pred ==0 else "Purchased")