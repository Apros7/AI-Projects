from dataclasses import dataclass
from typing import Dict, Hashable

@dataclass
class Node:
    value : int
    next : 'Node' | None
    prev : 'Node' | None

class LRU:
    length : int
    head : Node | None
    prev : Node | None

    lookup: Dict[Hashable, Node]
    reverse_lookup: Dict[Node, Hashable]

    def __init__(self, capacity : int = 10) -> None:
        self.length = 0
        self.head = self.tail = None
        lookup = Dict[Hashable, Node]
        reverse_lookup = Dict[Node, Hashable]
        self.capacity = capacity

    def update(self, key, value : int) -> None:
        node = self.lookup.get(key)
        if node is None:
            node = Node(value = value)
            self.length += 1
            self._prepend(node)
            self._trimCache()
        else:
            self._detach(node)
            self._prepend(node)

    def get(self, key) -> int | None:
        node = self.lookup.get(key)
        if node is None:
            return None
        self._detach(node)
        self._prepend(node)
        return node.value

    def _detach(self, node : Node) -> None:
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if self.head == node:
            self.head = self.head.next

        if self.tail == node:
            self.tail = self.tail.prev

        node.prev = None
        node.next = None

    def _prepend(self, node : Node) -> None:
        if self.head == None:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def _trimCache(self) -> None:
        pass
