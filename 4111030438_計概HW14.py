# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:55:12 2023

@author: User
"""

def quick_sort(arr):
    # 最好情況：O(n log n)，最壞情況：O(n^2)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    # 最好情況：O(n log n)，最壞情況：O(n log n)
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def bubble_sort(arr):
    # 最好情況：O(n)，最壞情況：O(n^2)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    # 最好情況：O(n)，最壞情況：O(n^2)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    # 測試數列
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Quick Sort
    sorted_arr_quick = quick_sort(arr.copy())
    print(f"Quick Sort: Best Case: O(n log n), Worst Case: O(n^2)\nSorted Array: {sorted_arr_quick}\n")

    # Merge Sort
    sorted_arr_merge = merge_sort(arr.copy())
    print(f"Merge Sort: Best Case: O(n log n), Worst Case: O(n log n)\nSorted Array: {sorted_arr_merge}\n")

    # Bubble Sort
    sorted_arr_bubble = bubble_sort(arr.copy())
    print(f"Bubble Sort: Best Case: O(n), Worst Case: O(n^2)\nSorted Array: {sorted_arr_bubble}\n")

    # Insertion Sort
    sorted_arr_insertion = insertion_sort(arr.copy())
    print(f"Insertion Sort: Best Case: O(n), Worst Case: O(n^2)\nSorted Array: {sorted_arr_insertion}\n")

if __name__ == "__main__":
    main()
