# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:10:02 2023

@author: User
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 讀取資料集
url = "https://www.kaggle.com/datasets/prasad22/healthcare-dataset"

data = pd.read_csv('healthcare_dataset.csv')

# 選擇特徵欄位和目標欄位
X_columns = ['Gender', 'Blood Type', 'Medical Condition', 'Admission Type', 'Medication']
Y_column = 'Test Results'
X = data[X_columns]
Y = data[Y_column]

label_encoder = LabelEncoder()

# 對每個類別欄位進行轉換
for column in X_columns:
    X.loc[:, column] = label_encoder.fit_transform(X[column].copy())

# 將目標欄位轉換為數值
Y = label_encoder.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, Y_train)

Y_pred = clf.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:", accuracy)
