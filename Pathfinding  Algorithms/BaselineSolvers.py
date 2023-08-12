
# Dijkstra algorithm does not really make sense in this simple current environment
# I have made some modifications, which makes it a pretty stupid algorithm, but gives a valid baseline.
# Could be adjusted and improved for later modifications if the environment changes.

import random
class BaselineSolver():
    def __init__(self, start_node, target_node, cols, rows, selection_function):
        self.start_node = start_node
        self.target_node = target_node
        self.cols = cols
        self.rows = rows
        self.selection_function = selection_function
        self.optimal_path_found = False
        self.checked_nodes = [self.start_node]
        self.moves = 0
    
    def one_step(self, grid):
        if self.optimal_path_found: return None
        avaliable_nodes = self.get_avaliable_nodes(grid)
        if len(avaliable_nodes) == 0: return None
        chosen_node = self.selection_function(avaliable_nodes)
        if self.finished(chosen_node, grid): return None
        self.checked_nodes.append(chosen_node)
        self.moves += 1
        return chosen_node

    def finished(self, node, grid): 
        if grid[node[0], node[1]] == 3: self.print_finish_statement(); self.optimal_path_found = True; return True
        return False

    def print_finish_statement(self): print(f"I ({self.__class__.__name__}) have now finished in {self.moves} moves.")

    def get_avaliable_nodes(self, grid):
        # utility function to get all currently possible moves
        avaliable_nodes = []
        for node in self.checked_nodes:
            neighbor_nodes = [(node[0] - 1, node[1]), (node[0] + 1, node[1]), (node[0], node[1] - 1), (node[0], node[1] + 1)]
            avaliable_nodes += neighbor_nodes
        set_nodes = list(set(avaliable_nodes))
        final_nodes = [node for node in set_nodes if self.is_node_in_workspace(node) and self.is_node_avaliable(node, grid)]
        return final_nodes
    
    def is_node_avaliable(self, node, grid):
        if grid[node[0], node[1]] in [0, 3]: return True

    def is_node_in_workspace(self, node):
        if node[0] >= self.rows or node[0] < 0: return False
        if node[1] >= self.cols or node[1] < 0: return False
        return True

class RandomBaselineSolver(BaselineSolver):
    def __init__(self, start_node, target_node, cols, rows) -> None:
        super().__init__(start_node, target_node, cols, rows, self.random_selection_function)

    def random_selection_function(self, avaliable_nodes): return random.choice(avaliable_nodes)

class CircleBaselineSolver(BaselineSolver):
    def __init__(self, start_node, target_node, cols, rows) -> None:
        super().__init__(start_node, target_node, cols, rows, self.circle_selection_function)

    def circle_selection_function(self, avaliable_nodes): 
        distances = [(node, self.get_distance(node)) for node in avaliable_nodes]
        return min(distances, key= lambda x: x[1])[0]

    def get_distance(self, node): return (node[0] - self.start_node[0])**2 + (node[1] - self.start_node[1])**2