from dataclasses import dataclass
from typing import List
import numpy as np

def walk(graph: np.ndarray, curr : int, needle : int, seen : List[bool], path : List[int]) -> bool:
    if seen[curr]:
        return False

    seen[curr] = True

    path.append(curr)

    if curr == needle:
        return True

    list = graph[curr]
    for i in range(len(list)):
        edge = list[i]
        if walk(graph, edge["to"], needle, seen, path):
            return True
        

    path.pop()

    return False

def dfs(
    adjacencyList: np.ndarray,
    source : int,
    needle : int
) -> List[int] | None:
    seen = np.zeros(len(adjacencyList), dtype=bool)
    path = []
    walk(adjacencyList, source, needle, seen, path)

    if len(path) == 0:
        return None
    return path