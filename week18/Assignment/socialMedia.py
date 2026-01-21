import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report)
import matplotlib.pyplot as plt
import seaborn as sns


rawData = pd.read_csv("Social_Network_Ads.csv")

le = LabelEncoder()
purchasedEncoded = le.fit_transform(rawData['Purchased'])
label_mapping = {0: 'Not Purchase', 1: 'Purchase'}
purchasedLabeled = pd.Series(purchasedEncoded).map(label_mapping)

X = rawData[['Age','EstimatedSalary']]
Y = purchasedEncoded

xtrain, xtest, ytrain, ytest = train_test_split(X,Y, test_size=0.2, random_state=10)

model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(xtrain, ytrain)

ypredit = model.predict(xtest)
cm = confusion_matrix(ytest, ypredit)

sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', 
            xticklabels=['Not Purchase', 'Purchase'],
            yticklabels=['Not Purchase', 'Purchase'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.show()

print("Confusion Matrix : ",cm)
print("Accuracy Score : ", accuracy_score(ytest,ypredit))
print("precision_score : ", precision_score(ytest,ypredit, zero_division=0))
print("recall_score : ", recall_score(ytest,ypredit, zero_division=0))
print("f1_score : ", f1_score(ytest,ypredit, zero_division=0))

print(classification_report(
    ytest,
    ypredit,
    target_names=['Not Purchase', 'Purchase']
))

userAge = int(input("Enter the age of the customer : "))
userEstimatedSalary = int(input("Enter estimated salary of the customer : "))
userInput = pd.DataFrame([[userAge, userEstimatedSalary]], columns=['Age', 'EstimatedSalary'])
prediction = model.predict(userInput)
predicted_label = label_mapping[prediction[0]]
print(predicted_label)



"""
1. Why is Logistic Regression suitable for this problem?
here the dependent variable is a prediction - 0 or 1 which decides whether the customer will purchase or not. if we have one or more independent variable and one dependent variable which is label, then logisticRegression is the best approach

2. What does Precision indicate in a business context?
Precision indicate = TP/(TP+FP).
Precision is used to indicate how much positives(purchased) are actually purchased.
If the precision is higher then if the model detects the positive purchases correctly

3. What does Recall indicate in a business context? 
Recal meaning TP/(TP+FN)
It indicate Out of all actual Positive cases, how many did the model successfully identify?
Recall can identify most of the not purchased ones

4. If Precision is high but Recall is low, what does it mean?
high precision meaning the model predicting Purchase correctly but it misses many actual customers who will purchase
"""