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

    lookup: dict
    reverse_lookup : dict

    def __init__(self, capacity : int = 10) -> None:
        self.length = 0
        self.head = self.tail = None
        lookup: Dict[Hashable, Node]
        reverse_lookup: Dict[Node, Hashable]
        self.capacity = capacity

    def update(self, key, value : int) -> None:
        pass

    def get(self, key) -> int | None:
        node = self.lookup.get(key)
        if node is None:
            return None
        self._detach(node)
        self._prepend(node)
        return node.value

    def _detach(self, node):
        pass

    def _prepend(self, node):
        pass
