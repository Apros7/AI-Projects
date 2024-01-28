
# weak ordered - not perfectly ordered
# Full tree (Always complete, no gaps or holes) - always filled from left to right
# MinHeap: Minimum value is root
# MaxHeap: Max value is root
# Could be done using nodes and making a tree using parents/childs, but ArrayList is much faster

class MinHeap:
    def __init__(self) -> None:
        self.data = []
        self.length = 0

    def insert(self, value : int) -> None:
        self.data[self.length] = value
        self._heapifyUp(self.length)
        self.length += 1

    def delete(self) -> int | None:
        if self.length == 0:
            return None

        out = self.data[0]
        if self.length == 1:
            self.data = []
            return out
        
        self.length -= 1
        self.data[0] = self.data[self.length]
        self._heapifyDown(0)
        return out

    def _heapifyDown(self, idx : int) -> None:
        leftIdx = self._leftChild(idx)
        rightIdx = self._rightChild(idx)
        
        if idx >= len(self.data) or leftIdx >= len(self.data):
            return None

        rightValue = self.data[rightIdx]
        leftValue = self.data[leftIdx]
        value = self.data[idx]

        if leftValue > rightValue and value > rightValue:
            self.data[idx], self.data[rightIdx] = self.data[rightIdx], self.data[idx]
            self._heapifyDown(rightIdx)

        elif rightValue > leftValue and value > leftValue:
            self.data[idx], self.data[leftIdx] = self.data[leftIdx], self.data[idx]
            self._heapifyDown(leftIdx)

    def _heapifyUp(self, idx : int) -> None:
        if idx == 0: 
            return None
        parent = self._parent(idx)
        parentValue = self.data[parent]
        value = self.data[idx]

        if parentValue > value:
            self.data[parent], self.data[idx] = self.data[idx], self.data[parent]
            self._heapifyUp(parent)

    

    def _parent(self, idx : int) -> int:
        return (idx - 1)//2

    def _leftChild(self, idx : int) -> int:
        return 2 * idx + 1
    
    def _rightChild(self, idx : int) -> int:
        return 2 * idx + 2
    
