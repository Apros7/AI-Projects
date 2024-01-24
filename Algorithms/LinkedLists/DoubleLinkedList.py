from typing import List
from dataclasses import dataclass

@dataclass
class Node():
    value: int
    next : 'Node' = None
    prev : 'Node' = None

class DoubleLinkedList():
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    def prepend(self, item: int) -> None:
        node = Node(value = item)
        self.length += 1
        if not self.head:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        return

    def insertAt(self, item : int, idx : int) -> None:
        if idx > self.length:
            raise IndexError("Cannot insert out of list")
        elif idx == self.length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return 
        
        self.length += 1
        curr = self._getAt(idx)

        node = Node(value = item)
        node.next = curr
        node.prev = curr.prev
        curr.prev.next = node
        if node.prev:
            node.prev.next = node # might be bug

    def append(self, item : int) -> None:
        node = Node(value = item)
        self.length += 1
        if not self.tail:
            self.head = self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        return 

    def remove(self, item : int) -> None:
        curr = self.head
        for i in range(self.length):
            if curr.value == item:
                break
            curr = curr.next
        if not curr:
            return 

        return self._removeNode(curr)

    def get(self, idx : int) -> int | None:
        return self._getAt(idx).value if self._getAt(idx) else None

    def removeAt(self, idx : int) -> int | None:
        node = self._getAt(idx)
        if not node:
            return
        return self._removeNode(node)
        
    def _removeNode(self, node : Node) -> int | None:
        self.length -= 1
        if self.length == 0:
            out = self.head.value if self.head else None
            self.head = self.tail = None
            return out
            
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next
        
        if node == self.tail:
            self.tail = node.prev

        node.prev = node.next = None
        return node.value

    def _getAt(self, idx : int) -> Node | None:
        curr = self.head
        for i in range(idx):
            if not curr: raise ValueError("Item in list is not a Node")
            curr = curr.next
        return curr

    def get_list(self) -> list:
        arr = [self.head]
        curr = self.head

        for i in range(self.length):
            curr = curr.next
            arr.append(curr)
        
        return arr
        
