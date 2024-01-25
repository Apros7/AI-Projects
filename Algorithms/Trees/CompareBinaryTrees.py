from dataclasses import dataclass
from typing import Optional

@dataclass
class BinaryNode():
    value : int | None
    right : Optional['BinaryNode'] = None
    left : Optional['BinaryNode'] = None

def compare_binary_trees(a : BinaryNode | None, b : BinaryNode | None) -> bool:
    if not a and not b:
        return True
    
    if not a or not b:
        return False

    if a.value != b.value:
        return False

    return compare_binary_trees(a.left, b.left) and compare_binary_trees(a.right, b.right)