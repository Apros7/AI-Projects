
from dataclasses import dataclass
from typing import List

direction = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

@dataclass
class Point():
    x: int
    y: int


def walk(maze : List[str], wall : str, curr : Point, end : Point, seen : List[List[bool]], path : List[Point]) -> bool:
    if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
        return False
    elif maze[curr.y][curr.x] == wall:
        return False
    elif curr.x == end.x and curr.y == end.y:
        path.append(curr)
        return True
    elif seen[curr.y][curr.x]:
        return False

    path.append(curr)
    seen[curr.y][curr.x] = True

    for i in range(len(direction)):
        x_, y_ = direction[i]
        new_curr = Point(x = curr.x + x_, y = curr.y + y_)
        if walk(maze, wall, new_curr, end, seen, path):
            return True

    path.pop()
    
    return False


def solve_maze(maze : List[str], wall : str, start : Point, end : Point) -> List[Point]:
    seen = [[False] * len(maze_i) for maze_i in maze]
    path = []
    walk(maze, wall, start, end, seen, path)
    return path

