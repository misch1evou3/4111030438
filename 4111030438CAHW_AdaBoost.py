# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:04:57 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from sklearn.ensemble import AdaBoostClassifier

#Load the MNIST dataset.
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#Reshape and normalize the data.
X_train = X_train.reshape(len(X_train), -1)
X_test = X_test.reshape(len(X_test), -1)

X_train = X_train.astype('float32')/255.
X_test = X_test.astype('float32')/255.

#Initialize the AdaBoost classifier.
ada = AdaBoostClassifier(n_estimators=100)

#Train the AdaBoost classifier on the training data.
ada.fit(X_train, y_train)

#Evaluate the AdaBoost classifier on the test data.
score = ada.score(X_test, y_test)
print('Accuracy:', score)

#Plot the misclassified images.

# Select misclassified images
misclassified_idx = np.where(ada.predict(X_test) != y_test)[0]

# Plot misclassified images
num_samples = 10
selected_images = X_test[misclassified_idx][:num_samples]
selected_labels = y_test[misclassified_idx][:num_samples]

for i in range(3):
    plt.figure(figsize=(20,4))
    for index, (image, label) in enumerate(zip(selected_images, selected_labels)):
        plt.subplot(1, num_samples, index + 1)
        plt.imshow(image.reshape(28,28), cmap=plt.cm.gray)
        plt.title(f'Actual: {label}, Predicted: {ada.predict([image])[0]}')
        plt.axis('off')
    plt.show()