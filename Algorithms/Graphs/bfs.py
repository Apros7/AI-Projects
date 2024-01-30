from dataclasses import dataclass
from typing import List
import numpy as np

def bfs(
    graph: np.ndarray,
    source : int,
    needle : int
) -> List(int) | None:

    seen = np.zeros(graph.shape, dtype=bool)
    prev = np.full(graph.shape, -1)
    seen[source] = True
    queue = [source]

    while len(queue) > 0:
        curr = queue[0]
        queue = queue[1:]
        
        if curr == needle:
            break

        adjs = graph[:, curr]
        for i in range(len(graph)):
            if adjs[i] == 0:
                continue
            if seen[i]:
                continue
            seen[i] = True
            prev[i] = curr
            queue.append(i)
        
    curr = needle
    out = []
    while prev[curr] != -1: 
        out.append(curr)
        curr = prev[curr]

    if len(out) > 0:
        return [source] + reversed(out)
    return None


