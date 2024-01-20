# Given two crystal balls that break from some height, determine the smallest height from which they will break.
# Linear search is slow: O(N)
# Binary search does not really work. If the first half is true, then you only have 1 ball left, 
#   and will have to do linear search. Therefore O(1/2 N) = O(N)

# Optimized solution:
# Step sqrt(N) each time. If the ball breaks, do linear search from last safe point.
# Worst case: sqrt(N) + sqrt(N) = 2*sqrt(N)
# Time: O(sqrt(N))

def two_crystal_balls():
    pass