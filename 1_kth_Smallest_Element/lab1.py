
import numpy as np
import math
import time
import random

def partition(arr, pivot):
    """
    Divides array arr into 3 parts:
    - elements smaller than the pivot, 
    - elements equal to the pivot,
    - elements greater than the pivot
    """
    if not arr:
        return [], [], []
    left = []
    piv = []
    right = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            piv.append(arr[i])
    return left, piv, right


def quicksort_kth(arr, k):
    """
    Finds k-th smallest element of the array arr using quicksort algorithm.
    """
    if not arr:
        return None
    pivot = arr[0]
    left, piv, right = partition(arr, pivot)
    
    if len(left) >= k:
        return quicksort_kth(left, k)
    elif len(left) + len(piv) >= k:
        return pivot
    return quicksort_kth(right, k - len(left) - len(piv))


def kthSmallest(arr, k, n):
    """
    Finds k-th smallest element of the array arr using probabilistic algorithm.
    """
    # if len(arr) <= 1000:
    #     return quicksort_kth(arr, k)
    
    sample_size = max(10, len(arr)//1000)
    sample = random.choices(arr, k = sample_size) 

    L1_index = max(1, int(sample_size * k / n - sample_size//50))
    L2_index = max(1, min(sample_size - 1, int(sample_size * k / n + sample_size//50)))
    
    L1 = quicksort_kth(sample, L1_index)
    L2 = quicksort_kth(sample, L2_index)

    left, l1_list, center_right = partition(arr, L1)
    center, l2_list, right = partition(center_right, L2)

    if len(left) < k <= len(left) + len(l1_list) + len(center):
        return quicksort_kth(l1_list + center, k - len(left))
    elif len(left) >= k:
        return kthSmallest(left, k, len(left))
    return kthSmallest(l2_list + right, k - len(left) - len(l1_list) - len(center), len(l2_list) + len(right))


def main():
    start = time.time()
    with open("in5.txt", "r") as file:
        lines = file.readlines()
    read_time = time.time() - start

    for i in range(int(lines[0])):
        arr = list(map(int, lines[2*i + 2].split()))
        k = int(lines[2*i+1].split()[1])
        n = int(lines[2*i+1].split()[0])
        print(f"List {i + 1}")
        print(f"k: {k}")
 
        start = time.time()
        answer_quicksort = quicksort_kth(arr, k)
        quicksort_time = time.time() - start

        start = time.time()
        answer_prob = kthSmallest(arr, k, n)
        prob_time = time.time() - start

        print(f"Read time: {read_time}")
        print(f"Quicksort - Answer: {answer_quicksort}")
        print(f"Quicksort - Time: {quicksort_time}")
        print(f"Probabilistic algorithm - Answer: {answer_prob}")
        print(f"Probabilistic algorithm - Time: {prob_time}")


if __name__ == "__main__":
    main()
