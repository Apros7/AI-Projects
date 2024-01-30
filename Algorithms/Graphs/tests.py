import numpy as np
from bfs import bfs

def test_bfs():
    matrix = np.array([
        [0, 1, 4, 5, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 2, 0],
        [0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0]
    ])
    assert bfs(matrix, 4, 0) == None
    assert bfs(matrix, 1, 2) == [1, 0, 2]
    assert bfs(matrix, 0, 4) == [0, 3, 4] or bfs(matrix, 0, 4) == [0, 2, 3, 4]

def test_dfs():
    AdjacencyList = [
        [{}]
    ]

if __name__ == "__main__":
    test_bfs()