
from dataclasses import dataclass
from typing import Optional

@dataclass
class BinaryNode():
    value : int | None
    right : Optional['BinaryNode'] = None
    left : Optional['BinaryNode'] = None

def search(curr: BinaryNode | None, needle : int) -> bool:

    if not curr:
        return False

    if curr.value == needle:
        return True

    if curr.value < needle:
        return search(curr.right, needle)

    return search(curr.left, needle)

def dfs(head : BinaryNode | None, needle : int):
    # depth-first search
    return search(head, needle)