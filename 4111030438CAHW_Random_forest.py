# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:03:02 2023

@author: User
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from keras.datasets import mnist
import matplotlib.pyplot as plt

    
# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()
  
# Reshape the data into a suitable format for Random Forest
n_samples = len(X_train)
X_train = X_train.reshape((n_samples, -1))
X_test = X_test.reshape((len(X_test), -1))
    
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
  
# Create a Random Forest classifier
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
    
# Train the Random Forest classifier
random_forest.fit(X_train, y_train)
    
# Make predictions on the test set
y_pred = random_forest.predict(X_test)
  
# Evaluate the performance of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))
  
# Visualize the prediction results
num_samples = 10
selected_images = X_test[:num_samples]
selected_labels = y_test[:num_samples]
selected_predictions = y_pred[:num_samples]

for i in range(3):
  plt.figure(figsize=(20, 4))
  for index, (image, label, prediction) in enumerate(zip(selected_images, selected_labels, selected_predictions)):
    plt.subplot(1, num_samples, index + 1)
    plt.imshow(image.reshape(28, 28), cmap=plt.cm.gray)
    plt.title(f'Actual:{label}, Predicted:{prediction}')
    plt.axis('off')
  plt.show()
