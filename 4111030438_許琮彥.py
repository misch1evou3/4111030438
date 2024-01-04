# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:10:04 2024

@author: User
"""


list_A = [99, 5, 33, 9, 8 ,12, 57, 64, 28, 1]



def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
            
def merge_sort(left, right):
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
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def create_list(lst):
     i = 0
     n = len(lst)
     list_B = []
     while True:
         if i < n:
             if i == n-1:
                 list_B.append(lst[i])
                 break
             t = lst[i] + lst[i+1]
             list_B.append(lst[i])
             i = i+1
             list_B.append(t)
         else:
             break
     return list_B
 
arr = create_list(list_A)


def main():
    
    print(f"listB為:{arr}\n")
  
    quick = quick_sort(arr.copy())
    print(f"quick排序: {quick}\n")

   
    bubble = bubble_sort(arr.copy())
    print(f"bubble排序: {bubble}\n")

    
    insertion = insertion_sort(arr.copy())
    print(f"insertion排序: {insertion}\n")
    
    merge = merge_sort(arr.copy())
    print(f"merge排序: {merge}\n")
    
    

if __name__ == "__main__":
    main()

        
    
    