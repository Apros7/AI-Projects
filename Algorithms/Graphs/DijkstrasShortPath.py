import numpy as np
from typing import List

def hasUnvisited(seen : List[bool], dists : List[int]) -> bool:
    return any(not s and dists[i] < 1000 for i, s in enumerate(seen))

def getLowestUnvisited(seen : List[bool], dists : List[int]) -> int:
    idx = -1
    lowestDistance = 10000
    for i in range(len(seen)):
        if seen[i]:
            continue
        if lowestDistance > dists[i]:
            lowestDistance = dists[i]
            idx = i
    return idx

def shortestPath(source : int, sink : int, AdjacencyList : np.ndarray) -> List[int]:
    seen = np.zeros(len(AdjacencyList), dtype=bool)
    prev = np.full(len(AdjacencyList), -1)
    dists = np.full(len(AdjacencyList), 10000)
    dists[source] = 0
    
    while hasUnvisited(seen, dists):
        curr = getLowestUnvisited(seen, dists)
        seen[curr] = True
        adjs = AdjacencyList[curr]
        for edge in adjs:
            if seen[edge["to"]]:
                continue
            dist = dists[curr] + edge["weight"]
            if dist < dists[edge["to"]]:
                dists[edge["to"]] = dist
                prev[edge["to"]] = curr
    
    out = []
    curr = sink
    while prev[curr] != -1:
        out.append(curr)
        curr = prev[curr]

    return [source] + list(reversed(out))
