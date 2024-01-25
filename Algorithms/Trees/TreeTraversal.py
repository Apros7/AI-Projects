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

def visitNode(node : BinaryNode): 
    if not node.right and not node.left:
        return [node.value]
    lst = []
    if node.right:
        lst.extend(visitNode(node.right))
    if node.left:
        lst.extend(visitNode(node.left))
    lst.append(node.value)
    return lst

def binary_tree_traversal(root_node : BinaryNode):
    return visitNode(root_node)