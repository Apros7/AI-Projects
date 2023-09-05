
from BaselineSolvers import BaselineSolver

# A* calculates the total cost, f = g + h
# g: distance between node and starting node
# h: heuristic: estimated distance from the current node to the end node.

class AstarSolver(BaselineSolver):
    def __init__(self, start_node, target_node, cols, rows) -> None:
        super().__init__(start_node, target_node, cols, rows, self.random_selection_function)

    def random_selection_function(self, avaliable_nodes): 
        distance_to_start_node = [(node, self.get_distance(node, self.start_node)) for node in avaliable_nodes]
        heuristic_to_target_node = [(node, self.get_distance(node, self.target_node)) for node in avaliable_nodes]
        total_cost = [(g[0], g[1] + h[1]) for g, h in zip(distance_to_start_node, heuristic_to_target_node)]
        return min(total_cost, key=lambda x: x[1])[0]
        
    def get_distance(self, node1, node2): return abs(node1.pos[0] - node2.pos[0]) + abs(node1.pos[1] - node2.pos[1])