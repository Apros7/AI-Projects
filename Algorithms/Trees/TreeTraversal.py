from dataclasses import dataclass
from typing import Optional

@dataclass
class Node():
    value : int | None
    children : list | None = None

@dataclass
class BinaryNode():
    value : int | None
    right : Optional['BinaryNode'] = None
    left : Optional['BinaryNode'] = None

def visitNode(node : BinaryNode, path : list) -> None | list: 
    if not node:
        return

    path.append(node.value)
    visitNode(node.right, path)
    visitNode(node.left, path)
    return path

def binary_tree_traversal(root_node : BinaryNode): # depth first search
    return visitNode(root_node, [])

def find_needle_breadth_first_search(root_node : BinaryNode, needle : int) -> bool:
    # Array gives O(n^2)
    # Queue gives O(n)
    # Therefore a Queue must be implemented
    queue = [root_node]

    while len(queue) > 0:
        curr = queue[0]
        if curr.value == needle:
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return False

    