from dataclasses import dataclass

@dataclass
class Node():
    value: int
    prev : 'Node' = None

class Stack:
    length: int
    _head: Node
    _tail: Node

    def __init__(self):
        self._head = self._tail = None
        self.length = 0

    def push(self, value : int) -> None:
        node = Node(value)
        if self._head is None:
            self._head = self._tail = node
        node.prev = self._head
        self._head = node
        self.length += 1

    def pop(self) -> Node | None:
        if self._head is None: return None
        prev_head = self._head
        self._head = self._head.prev
        self.length -= 1
        if self.length == 0: self._tail = None
        return prev_head

    def peek(self) -> Node | None:
        return self._head

    def __len__(self):
        return self.length