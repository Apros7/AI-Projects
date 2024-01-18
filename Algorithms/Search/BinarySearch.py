import numpy as np

def binary_search(arr, v):
    # Big O: Log_2(N)
    rounds = np.log2(len(arr))
    for _ in rounds:
        if len(arr) == 1 and v != arrv: return False
        middle = len(arr)//2
        arr1, arrv, arr2 = arr[:middle], arr[middle], arr[middle+1:]
        if v == arrv: return True
        if v > arrv: arr = arr1
        arr = arr2
    return False