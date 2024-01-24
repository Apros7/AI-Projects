
import pytest
from DoubleLinkedList import DoubleLinkedList

def test_double_linked_list():
    linked_list = DoubleLinkedList()
    assert linked_list.head == None
    assert linked_list.prepend(3) == None
    assert linked_list.head.value == 3 and linked_list.tail.value == 3
    linked_list.append(4)
    linked_list.insertAt(5, 1)
    assert linked_list.get_list() == [3, 5, 4]
    linked_list.append(8)
    linked_list.prepend(4)
    linked_list.removeAt(1)
    assert linked_list.get_list() == [4, 5, 4, 8]
    linked_list.remove(5)
    assert linked_list.get_list() == [4, 4, 8]
    assert linked_list.remove(85) == None
    assert linked_list.get_list() == [4, 4, 8]
    with pytest.raises(IndexError):
        linked_list.insertAt(10, 10)


if __name__ == "__main__":
    test_double_linked_list()