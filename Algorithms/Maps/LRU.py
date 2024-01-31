from dataclasses import dataclass
from typing import Dict, Hashable, Optional

@dataclass
class Node:
    value : int
    next : Optional['Node'] = None
    prev : Optional['Node'] = None

class LRU:
    length : int
    head : Node | None
    prev : Node | None

    lookup: Dict[Hashable, Node]
    reverseLookup: Dict[Node, Hashable]

    def __init__(self, capacity : int = 10) -> None:
        self.length = 0
        self.head = self.tail = None
        self.lookup = {}
        self.reverseLookup = {}
        self.capacity = capacity

    def update(self, key, value : int) -> None:
        node = self.lookup.get(key)
        if node is None:
            node = Node(value = value)
            self.length += 1
            self._prepend(node)
            self._trimCache()
            self.lookup[key] = node
            self.reverseLookup[self._nodeAsDict(node)] = key
        else:
            self._detach(node)
            self._prepend(node)
            node.value = value

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
        if self.length <= self.capacity:
            return
        tail = self.tail
        self._detach(tail)
        key = self.reverseLookup.get(self._nodeAsDict(tail))
        self.lookup.pop(key)
        self.reverseLookup.pop(self._nodeAsDict(tail))

    def _nodeAsDict(self, node : Node) -> None: # This is definitely not ideal, if some Nodes have the same value, this breaks
        return f"{node.value}"
