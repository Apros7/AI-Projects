from BubbleSort import bubble_sort
from Queue import Queue, Node
from Stack import Stack

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

if __name__ == "__main__":
    test_bubble_sort()
    test_node()
    test_queue()
    test_stack()