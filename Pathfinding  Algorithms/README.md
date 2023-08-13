Throught it would be nice to visualize some pathfinding algorithms and study how they work, so I made this.

To run the simulation run:
```
python3 simulation.py
```

This will run both baseline solvers, first the random, then the circular one. You need to close the app to move on the next.

## Baseline Simulation
The simulation will sometimes produce unsolveable simulations.
All obstacles, start and end position is known from the start
Map is currently 25 x 40 tiles. The starting position is always in the first 10 rows, and the end position in the last 10 rows.


### Algorithms used:
- BaselineSolvers: Both a random and a circular solver. CircleBaselineSolver is basically the theory behind [Dijkstra’s algorithm](https://www.graphable.ai/blog/pathfinding-algorithms/), but since there is no difference in the length between nodes, this becomes a simple circular solver more like [Breadth First Search](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- Heuristic Solver: Chooses the node with the shortest distance to the target node.
- [A*](https://www.geeksforgeeks.org/a-search-algorithm/): Dependent on knowing the end point to work. Large improvement over BaselineSolvers

Random Solver: | Circular Solver: | Heuristic Solver | A Star Solver |
:-------------:|:----------------:|:----------------:|:-------------:
Finished in 399 moves | Finished in 470 moves | Finished in 68 moves | None
Chosen path is 52 moves | Chosen path is 46 moves | Chosen path is 48 moves | None
![](recordings/random_solver.gif) | ![](recordings/circle_solver.gif) | ![](recordings/heuristic_solver.gif) | None

## More challenging simulations:
Only tiles 5 distance away from a visited tile can be seen.

### Fog

## Notes for myself
- Maybe train some deep RL on this?
- Could be fun to add fog to the agent and visualize with fog? Make a game where it should rescue unknown amounts of people?
- Maybe make some red stations, which are the only places the AI can choose to go, although the aim should still be to travel the least amount of tiles overall.
- Maybe make some forests, lakes that takes longer to get through?
- I also need to make the actual route and showcase it