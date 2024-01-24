from BubbleSort import bubble_sort
from Queue import Queue, Node
from Stack import Stack
from QuickSort import quicksort

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
    assert len(queue) == 0
    assert queue.enqueue(5) is None
    queue.enqueue(Node(3))
    assert len(queue) == 2
    assert queue.peek() == 5
    assert queue.deque().value == Node(5).value

def test_stack():
    from Stack import Node
    stack = Stack()
    assert stack.peek() is None
    assert stack.pop() is None
    assert len(stack) == 0
    assert stack.push(5) is None
    stack.push(3)
    assert len(stack) == 2
    assert stack.peek().value == Node(3).value
    assert stack.pop().value == Node(3).value

def test_quicksort():
    arr = [9, 3, 7, 4, 69, 420, 42]
    quicksort(arr)
    sorted_should_be = [3, 4, 7, 9, 42, 69, 420]
    assert arr == sorted_should_be

if __name__ == "__main__":
    test_bubble_sort()
    test_node()
    test_queue()
    test_stack()
    test_quicksort()

# Benefit of array is search: Only LinearSearch is available for LinkedLists
# Benefit of LinkedList: Easy to delete and shift (example of a queue) - would perform poorly with array
# RingBuffer: Array, but if the tail goes to the end, you will just go to the front again i.e implementing a queue in an array
# Allows for constant time both adding and deleting at head and tail.
# Object pool: Instead of creating objects for each user, create the object, set the param, use it, hand back to pool to set new param.
# In js ArrayList is used (un/shift is slow, push/pop/get is fast)