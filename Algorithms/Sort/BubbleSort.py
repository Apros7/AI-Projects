
# Bubble Sort
# Slow: (N * (N + 1)) / 2 = O(N^2 + N) = O(N^2)

from typing import List

def bubble_sort(arr : List[int]):
    for i in reversed(range(0, len(arr))):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr