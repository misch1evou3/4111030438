# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def bubble_sort(arr):
    n = len(arr)
    
    #遍歷整個數列
    for i in range(n):
        #最後i個元素已經排好序,不需要再比較
        for j in range(0, n-i-1):
            #比較相鄰的元素進行交換
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("第{}次遍歷後排序結果{}".format(i, arr))
    print("Bubble sort 後的數列:")
    print(arr)

def insertion_sort(arr):
    #從第二個元素開始遍歷
    for i in range(1, len(arr)):
        key = arr[i] #選擇當前要插入元素
        j = i-1
        
        #將比key大的元素往右移動
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        #將key插入到適當的位置    
        arr[j+1] = key
        print("第{}次遍歷後排序結果{}".format(i, arr))
    print("Insertion sort 後的數列:")
    print(arr)

example_array = [100, 64, 34, 25, 12, 22, 11, 90]
bubble_sort(example_array)
insertion_sort(example_array)
print()