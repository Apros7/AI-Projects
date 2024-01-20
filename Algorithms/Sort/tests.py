from BubbleSort import bubble_sort

import pytest

def test_bubble_sort():
    assert bubble_sort([1, 3, 7, 4, 2]) == [1, 2, 3, 4, 7]

if __name__ == "__main__":
    test_bubble_sort()