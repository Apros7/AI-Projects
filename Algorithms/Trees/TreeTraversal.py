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

def breadth_first_search(root_node : BinaryNode):
    # Array gives O(n^2)
    # Queue gives O(n)
    # Therefore a Queue must be implemented
    