from dataclasses import dataclass

@dataclass
class Node():
    value : int | None
    children : list | None = None

def visitNode(node : Node): 
    if not node.children:
        return [node.value]
    lst = []
    for child in node.children:
        lst.extend(visitNode(child))
    lst.append(node.value)
    return lst

def tree_traversal_left(root_node : Node):
    return visitNode(root_node)