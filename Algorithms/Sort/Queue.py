
from typing import List
from dataclasses import dataclass

@dataclass
class Node():
    value: int
    next : 'Node' = None

class Queue():
    """
    A LinkedList but with constraints to ensure high performance
    """
    length : int
    _head : Node or None
    _tail : Node or None

    def __init__(self) -> None:
        self._head = self._tail = None
        self.length = 0

    def enqueue(self, value : int) -> None:
        node = Node(value)
        if self._tail is None:
            self._head = self._tail = node
        self._tail.next = node
        self._tail = node
        self.length += 1

    def deque(self):
        if self._head is None: return None
        old_head = self._head
        self._head = self._head.next
        self.length -= 1
        return old_head

    def peek(self):
        return self._head.value if self._head is not None else None

    def __len__(self):
        return self.length