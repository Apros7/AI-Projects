
from TreeTraversal import BinaryNode, binary_tree_traversal

def test_binary_tree_traversal():
    node5, node4, node18, node21 = BinaryNode(5), BinaryNode(4), BinaryNode(18), BinaryNode(21)
    node23 = BinaryNode(23, node5, node4)
    node3 = BinaryNode(3, node18, node21)
    root_node = BinaryNode(7, node23, node3)
    assert binary_tree_traversal(root_node) == [5, 4, 23, 18, 21, 3, 7]


if __name__ == "__main__": 
    test_binary_tree_traversal()