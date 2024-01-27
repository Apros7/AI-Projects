
# weak ordered - not perfectly ordered
# Full tree (Always complete, no gaps or holes) - always filled from left to right
# MinHeap: Minimum value is root
# MaxHeap: Max value is root
# Could be done using nodes and making a tree using parents/childs, but ArrayList is much faster

class MinHep:
    def __init__(self) -> None:
        self.data = []
        self.length = 0

    def insert(self, value : int) -> None:
        pass

    def remove(self) -> int:
        pass

    def _parent(self, idx : int) -> int:
        return (idx - 1)//2

    def _childs(self, idx : int) -> int:
        return (2 * idx + 1, 2 * idx + 2)
