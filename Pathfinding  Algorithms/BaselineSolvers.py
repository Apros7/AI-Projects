
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
        if self.finished(chosen_node, grid): self.path_length = len(chosen_node); return self.path_function(chosen_node)
        self.checked_nodes.append(chosen_node)
        self.moves += 1
        return chosen_node

    def path_function(self, chosen_node):
        path = []
        while True:
            if chosen_node.parent: path.append(chosen_node); chosen_node = chosen_node.parent
            else: break
        return path

    def finished(self, node, grid): 
        if grid[node.pos[0], node.pos[1]] == 3: self.print_finish_statement(); self.optimal_path_found = True; return True
        return False

    def print_finish_statement(self): print(f"I ({self.__class__.__name__}) have now finished in {self.moves} moves.")

    def get_avaliable_nodes(self, grid):
        # utility function to get all currently possible moves
        avaliable_nodes = []
        for parent_node in self.checked_nodes:
            neighbor_nodes = [(parent_node.pos[0] - 1, parent_node.pos[1]), (parent_node.pos[0] + 1, parent_node.pos[1]), 
                              (parent_node.pos[0], parent_node.pos[1] - 1), (parent_node.pos[0], parent_node.pos[1] + 1)]
            with_parent_nodes = [Node(parent_node, neighbor_node) for neighbor_node in neighbor_nodes]
            avaliable_nodes += with_parent_nodes
        final_nodes = [node for node in avaliable_nodes if self.is_node_in_workspace(node) and self.is_node_avaliable(node, grid)]
        return final_nodes
    
    def is_node_avaliable(self, node, grid):
        if grid[node.pos[0], node.pos[1]] in [0, 3]: return True

    def is_node_in_workspace(self, node):
        if node.pos[0] >= self.rows or node.pos[0] < 0: return False
        if node.pos[1] >= self.cols or node.pos[1] < 0: return False
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

    def get_distance(self, node): return (node.pos[0] - self.start_node.pos[0])**2 + (node.pos[1] - self.start_node.pos[1])**2

class HeuristicSolver(BaselineSolver):
    """
    Picks the avaliable node with the least distance to the end
    """
    def __init__(self, start_node, target_node, cols, rows) -> None:
        super().__init__(start_node, target_node, cols, rows, self.random_selection_function)

    def random_selection_function(self, avaliable_nodes): 
        heuristic_to_target_node = [(node, self.get_distance(node, self.target_node)) for node in avaliable_nodes]
        return min(heuristic_to_target_node, key=lambda x: x[1])[0]
        
    def get_distance(self, node1, node2): return (node1.pos[0] - node2.pos[0])**2 + (node1.pos[1] - node2.pos[1])**2

class Node():
    def __init__(self, parent, position): 
        self.parent = parent
        self.pos = position