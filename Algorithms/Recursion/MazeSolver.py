
from dataclasses import dataclass
from typing import List

@dataclass
class Point():
    x: int
    y: int

def walk(maze : List[str], wall : str, curr : Point, end : Point, seen : List[bool]) -> bool:
    if curr.x < 0 or curr.x > len(maze[0]) or curr.y < 0 or curr.y > len(maze):
        return False
    elif maze[curr.y][curr.x] == wall:
        return False
    elif curr.x == end.x and curr.y == end.y:
        return True
    elif seen[curr.y][curr.x]:
        return False


def solve_maze(maze : List[str], wall : str, start : Point, end : Point) -> List[Point]:
    pass
