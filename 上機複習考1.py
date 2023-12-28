# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:18:04 2023

@author: User
"""
# 定義 5 個 Tuple
tuples = [
    ("A", (7, 8, 9)),
    ("B", (2, 3, 2)),
    ("C", (3, 5, 1)),
    ("D", (3, 3, 9)),
    ("E", (6, 7, 8))
]

# 計算每個 Tuple 總和
sums = [sum(t[1]) for t in tuples]

# 印出未排序的情形
print("未排序:")
for i, (label, _) in enumerate(tuples):
    print(f"{label} : {sums[i]}")

# 使用 Quick sort 進行排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sorted_sums_quick = quick_sort(sums)

# 使用 Bubble sort 進行排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

sorted_sums_bubble = sums.copy()
bubble_sort(sorted_sums_bubble)

# 印出排序後的情形
print("\nQuick sort 排序:")
for i, label in enumerate(sorted_sums_quick):
    print(f"{tuples[i][0]} : {label}")

print("\nBubble sort 排序:")
for i, label in enumerate(sorted_sums_bubble):
    print(f"{tuples[i][0]} : {label}")
