from BubbleSort import bubble_sort
from Queue import Queue, Node

import pytest

def test_bubble_sort():
    assert bubble_sort([1, 3, 7, 4, 2]) == [1, 2, 3, 4, 7]

def test_node():
    assert Node(3).value == 3
    assert Node(2, Node(3, Node(5))).next.next.value == 5

def test_queue():
    queue = Queue()
    assert queue.peek() is None
    assert queue.deque() is None
    assert queue.enqueue(Node(5)) is None
    queue.enqueue(Node(3))
    assert len(queue) == 2
    assert queue.peek() == 5
    assert queue.deque() == Node(5)

if __name__ == "__main__":
    test_bubble_sort()
    test_node()