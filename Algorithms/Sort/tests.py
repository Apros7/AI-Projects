from BubbleSort import bubble_sort
from Queue import Queue

import pytest

def test_bubble_sort():
    assert bubble_sort([1, 3, 7, 4, 2]) == [1, 2, 3, 4, 7]

def test_queue():
    queue = Queue([2,5,4,5,2])
    assert queue.deque() == 2
    assert queue.peek() == 5

    queue = Queue([2,5,4,5,2])
    queue.enqueue(3)
    assert len(queue) == 6

if __name__ == "__main__":
    test_bubble_sort()