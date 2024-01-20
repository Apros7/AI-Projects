# Given two crystal balls that break from some height, determine the smallest height from which they will break.
# Linear search is slow: O(N)
# Binary search does not really work. If the first half is true, then you only have 1 ball left, 
#   and will have to do linear search. Therefore O(1/2 N) = O(N)

# Optimized solution:
# Step sqrt(N) each time. If the ball breaks, do linear search from last safe point.
# Worst case: sqrt(N) + sqrt(N) = 2*sqrt(N)
# Time: O(sqrt(N))

import math

def two_crystal_balls(arr : list(bool)):
    N = len(arr)
    for i in range(0, N, math.sqrt(N)):
        if arr[i]:
            return linear_search(arr[i+1:i+math.sqrt(N)+1])
    return False

def linear_search(arr : list, v : int):
    for i, el in enumerate(arr): 
        if el == v:
            return i
    return False