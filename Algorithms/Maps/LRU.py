from dataclasses import dataclass

@dataclass
class Node:
    value : int
    next : 'Node' | None
    next : 'Node' | None

class LRU:
    length : int

    def __init__(self) -> None:
        self.length = 0

    def update(self, key, value : int) -> None:
        pass

    def get(self, key) -> int | None:
        pass
