
from TreeTraversal import BinaryNode, binary_tree_traversal, find_needle_breadth_first_search
from CompareBinaryTrees import compare_binary_trees

def test_binary_tree_traversal():
    node5, node4, node18, node21 = BinaryNode(5), BinaryNode(4), BinaryNode(18), BinaryNode(21)
    node23 = BinaryNode(23, node5, node4)
    node3 = BinaryNode(3, node18, node21)
    root_node = BinaryNode(7, node23, node3)
    assert binary_tree_traversal(root_node) == [7, 23, 5, 4, 3, 18, 21]

def test_breadth_first_search():
    node5, node4, node18, node21 = BinaryNode(5), BinaryNode(4), BinaryNode(18), BinaryNode(21)
    node23 = BinaryNode(23, node5, node4)
    node3 = BinaryNode(3, node18, node21)
    root_node = BinaryNode(7, node23, node3)
    assert find_needle_breadth_first_search(root_node, 7)
    assert find_needle_breadth_first_search(root_node, 18)
    assert find_needle_breadth_first_search(root_node, 5)
    assert not find_needle_breadth_first_search(root_node, 89)
    assert not find_needle_breadth_first_search(root_node, 17)

def test_compare_binary_trees():
    pass

if __name__ == "__main__": 
    test_binary_tree_traversal()
    test_breadth_first_search()