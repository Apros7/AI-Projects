
from TreeTraversal import Node, tree_traversal_left

def test_tree_traversal():
    node5, node4, node18, node21 = Node(5), Node(4), Node(18), Node(21)
    node23 = Node(23, [node5, node4])
    node3 = Node(3, [node18, node21])
    root_node = Node(7, [node23, node3])
    assert tree_traversal_left(root_node) == [5, 4, 23, 18, 21, 3, 7]


if __name__ == "__main__": 
    test_tree_traversal()