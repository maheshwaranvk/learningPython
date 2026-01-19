import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report)


rawData = pd.read_csv("sales_data_logistic.csv")

le = LabelEncoder()
cardTypeEncoded = le.fit_transform(rawData['CardType'])
print(le.inverse_transform([0,1]))

x = rawData[['Total Amount']]
y = cardTypeEncoded

xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2, random_state=10)

model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(xtrain, ytrain)

ypredit = model.predict(xtest)

print("Confusion Matrix : ",confusion_matrix(ytest, ypredit))

print("Accuracy Score : ", accuracy_score(ytest,ypredit))
print("precision_score : ", precision_score(ytest,ypredit, zero_division=0))
print("recall_score : ", recall_score(ytest,ypredit, zero_division=0))
print("f1_score : ", f1_score(ytest,ypredit, zero_division=0))

print(classification_report(
    ytest,
    ypredit,
    target_names=le.classes_
))

userValue = int(input("Enter the Total Amount : "))
userInput = [[userValue]]
prediction = model.predict(userInput)
print (le.inverse_transform(prediction))