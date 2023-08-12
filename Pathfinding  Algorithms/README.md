Throught it would be nice to visualize some pathfinding algorithms and study how they work, so I made this.

To run the simulation run:
```
python3 simulation.py
```

This will run both baseline solvers, first the random, then the circular one. You need to close the app to move on the next.

<div class="gif-container">
    <div class="gif-column">
        <h1>Random Solver:</h1>
        <img src="recordings/random_solver.gif" alt="First GIF">
    </div>
    <div class="gif-column">
        <h1>Circular Solver:</h1>
        <img src="recordings/circle_solver.gif" alt="Second GIF">
    </div>
</div>

<style>
.gif-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
}

.gif-column {
    flex: 1;
}
</style>

## Current solvers:
- BaselineSolvers: Both a random and a circular solver. CircleBaselineSolver is basically the theory behind [Dijkstra’s algorithm](https://www.graphable.ai/blog/pathfinding-algorithms/), but since there is no difference in the length between nodes, this becomes a simple circular solver

## Notes for the future
- Maybe train some deep RL on this?
- Could be fun to add fog to the agent and visualize with fog?
- Maybe make some red stations, which are the only places the AI can choose to go, although the aim should still be to travel the least amount of tiles overall.
- Maybe make some forests, lakes that takes longer to get through?