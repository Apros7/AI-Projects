from LinearSearch import linear_search
from BinarySearch import binary_search
from TwoCrystalBalls import two_crystal_balls

import pytest

def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5, 6], 6)
    assert not linear_search([1, 2, 3, 4, 5, 6], "E")
    assert not linear_search([1, 2, 3, 4, 5, 6], 8)

def test_binary_search():
    assert binary_search(list(range(4096)), 56)
    assert not binary_search(list(range(4096)), 8000)
    assert binary_search(list(range(4096)), 3011)
    assert not binary_search(list(range(4096)), -1)
    with pytest.raises(TypeError):
        binary_search(list(range(4096)), "E")

def test_crystal_problem():
    assert two_crystal_balls([False, False, False, False, True, True, True, True, True]) == 4
    assert not two_crystal_balls([False, False, False, False])
    assert two_crystal_balls([False, False, False, False, True, True]) == 4

if __name__ == "__main__":
    test_linear_search()
    test_binary_search()
    test_crystal_problem()