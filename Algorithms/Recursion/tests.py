import pytest
from MazeSolver import Point, solve_maze

def test_maze():
    maze = [
        "#####E#",
        "#     #",
        "#S#####"
    ]
    wall = "#"
    start = Point(x = 1, y = 2)
    end = Point(5, 0)
    path = solve_maze(maze, wall, start, end)
    correct_path = [Point(x=1, y=2), Point(x=1, y=1), Point(x=2, y=1), Point(x=3, y=1), Point(x=4, y=1), Point(x=5, y=1), Point(x=5, y=0)]
    assert path == correct_path

if __name__ == "__main__":
    test_maze()