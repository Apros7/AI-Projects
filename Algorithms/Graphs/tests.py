import numpy as np
from bfs import bfs
from dfs import dfs
from DijkstrasShortPath import shortestPath

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
        [{"to": 1}, {"to": 2}, {"to": 3}],
        [{"to": 0}],
        [{"to": 3}],
        [{"to": 4}],
        []
    ]
    assert dfs(AdjacencyList, 4, 0) == None
    assert dfs(AdjacencyList, 1, 2) == [1, 0, 2]
    assert dfs(AdjacencyList, 0, 4) == [0, 3, 4] or dfs(AdjacencyList, 0, 4) == [0, 2, 3, 4]

def test_shortest_path():
    AdjacencyList = [
        [{"to": 1, "weight": 1}, {"to": 2, "weight": 5}],
        [{"to": 2, "weight": 7}, {"to": 3, "weight": 5}],
        [{"to": 4, "weight": 1}],
        [{"to": 2, "weight": 1}, {"to": 1, "weight": 1}],
        []
    ]
    assert shortestPath(4, 0, AdjacencyList) == [4]
    assert shortestPath(0, 2, AdjacencyList) == [0, 2]
    assert shortestPath(0, 4, AdjacencyList) == [0, 2, 4]

if __name__ == "__main__":
    test_bfs()
    test_dfs()
    test_shortest_path()