
def qs(arr : list, lo : int, hi : int) -> None:
    if lo >= hi:
        return

    pivotIdx = partition(arr, lo, hi)
    qs(arr, lo, pivotIdx - 1)
    qs(arr, pivotIdx + 1, hi)

def partition(arr : list, lo : int, hi : int) -> int:
    pivot = arr[hi]
    idx = lo - 1

    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]
    
    idx += 1
    arr[hi], arr[idx] = arr[idx], pivot

    return idx

def quicksort(arr : list) -> None:
    qs(arr, 0, len(arr) - 1)