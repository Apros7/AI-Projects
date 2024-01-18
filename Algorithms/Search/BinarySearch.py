import numpy as np

def binary_search(arr : list, v : int):
    if not isinstance(arr, list) or not isinstance(v, int):
        raise TypeError("One parameter is not of the correct time")
        # return False
    # Big O: Log_2(N)
    rounds = int(np.log2(len(arr)))
    for _ in range(rounds):
        if len(arr) == 1 and v != arr[0]: return False
        middle = len(arr)//2
        arr1, arrv, arr2 = arr[:middle], arr[middle], arr[middle+1:]
        if v == arrv: return True
        if v > arrv: arr = arr2
        else: arr = arr1
    return False