# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:49:59 2023

@author: User
"""

from keras.datasets import mnist
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

#載入手寫數字資料集
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#資料預處理
#資料轉成二維,以便進行聚類
X_train = X_train.reshape(len(X_train), -1)
X_test = X_test.reshape(len(X_test), -1)

#正規化資料
X_train = X_train.astype('float32')/255.
X_test = X_test.astype('float32')/255.

#初始化K均值模型,設定群組數量為10(因為手寫數字0~9共10個數字)
kmeans = KMeans(n_clusters=10, random_state=42)

#使用k均值模型對訓練資料進行擬合
kmeans.fit(X_train)

#選擇要顯示的數字圖片和對應的標籤
num_samples = 10
selected_images = X_train[:num_samples]
selected_labels = y_train[:num_samples]

#設定圖表的大小和列數
for i in range(3):
    plt.figure(figsize=(20,4))
    for index, (image, label) in enumerate(zip(selected_images, selected_labels)):
       #將每張圖片繪製在子圖上
       plt.subplot(1, num_samples, index + 1)
       plt.imshow(image.reshape(28,28), cmap=plt.cm.gray)
       plt.title(f'Cluster:{label}')
       plt.axis('off')
    plt.show()