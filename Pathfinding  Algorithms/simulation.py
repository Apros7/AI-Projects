import pygame
import numpy as np
import copy
import os

from BaselineSolvers import RandomBaselineSolver, CircleBaselineSolver, HeuristicSolver, Node
from A_star import AstarSolver

pygame.init()

# Setup:
record = False
tile_size = 25
number_tiles_horizontal = 40
number_tiles_vertical = 25
possible_columns_start_node = 5
possible_columns_end_node = 5
width = tile_size * number_tiles_horizontal
height = tile_size * number_tiles_vertical
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 15)

#clean folders
path = "/Users/lucasvilsen/Desktop/AI-FunProjects/Pathfinding  Algorithms/pictures"
if record:
    for folder in os.listdir(path):
        for file in os.listdir(path + "/" + folder):
            os.remove(path + "/" + folder + "/" + file) 

# colors:
colors_and_text = [
    ((255, 255, 255), None),    # normal block
    ((0,0,0), None),            # black, blocking block
    ((0,255,0), "Start"),       # start block
    ((30,144,255), "End"),      # end block
    ((255,215,0), None),        # tiles the algorithms has visited
    ((255,105,180), None)]      # the final path

def make_grid(): 
    grid = np.random.choice([0, 1], size=(number_tiles_vertical, number_tiles_horizontal), p=[0.6, 0.4])
    begin_point = (np.random.choice(range(number_tiles_vertical)), np.random.choice(list(range(number_tiles_horizontal))[:possible_columns_start_node]))
    end_point = (np.random.choice(range(number_tiles_vertical)), np.random.choice(list(range(number_tiles_horizontal))[-possible_columns_end_node:]))
    grid[begin_point[0], begin_point[1]] = 2
    grid[end_point[0], end_point[1]] = 3
    begin_node = Node(None, begin_point)
    end_node = Node(None, end_point)
    return grid, begin_node, end_node

def color_node(node, grid):
    grid[node.pos[0], node.pos[1]] = 4
    return grid

def color_path(nodes, grid):
    for node in nodes:
        grid[node.pos[0], node.pos[1]] = 5
    return grid

def init_solvers(begin_node, end_node, number_tiles_horizontal, number_tiles_vertical):
    random_solver = RandomBaselineSolver(start_node=begin_node, target_node=end_node, 
                                    cols=number_tiles_horizontal, rows=number_tiles_vertical)
    circle_solver = CircleBaselineSolver(start_node=begin_node, target_node=end_node, 
                                    cols=number_tiles_horizontal, rows=number_tiles_vertical)
    heuristic_solver = HeuristicSolver(start_node=begin_node, target_node=end_node, 
                                    cols=number_tiles_horizontal, rows=number_tiles_vertical) 
    a_star_solver = AstarSolver(start_node=begin_node, target_node=end_node, 
                                    cols=number_tiles_horizontal, rows=number_tiles_vertical)
    solvers = [random_solver, circle_solver, heuristic_solver, a_star_solver]
    return solvers

# Check that maze is possible to solve, else make new maze
def get_valid_grid(number_tiles_horizontal, number_tiles_vertical, info=True):
    while True:
        if info: print("Trying out maze...")
        grid, begin_node, end_node = make_grid()
        solvers = init_solvers(begin_node, end_node, number_tiles_horizontal, number_tiles_vertical)
        grid0 = copy.deepcopy(grid)
        solver = solvers[2] # currently best performing
        if info: print("Solver chosen: ", solver.__class__.__name__)
        returned = begin_node
        while not isinstance(returned, list) and returned != None:
            color_node(returned, grid)
            returned = solver.one_step(grid)
        if isinstance(returned, list): 
            if info: print("Found working maze")
            break
    return grid, grid0, begin_node, end_node

if __name__ == "__main__":
    # to visualize solvers, run this:
    grid, grid0, begin_node, end_node = get_valid_grid(number_tiles_horizontal, number_tiles_vertical)
    solvers = init_solvers(begin_node, end_node, number_tiles_horizontal, number_tiles_vertical)
    for i, solver in enumerate(solvers):
        frame_count = 0
        running = True
        grid = copy.deepcopy(grid0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for row in range(number_tiles_vertical):
                for col in range(number_tiles_horizontal):
                    x = col * tile_size
                    y = row * tile_size
                    rect = pygame.Rect(x, y, tile_size, tile_size)
                    tile_image = pygame.Surface((tile_size, tile_size))
                    color, text = colors_and_text[grid[row, col]]
                    tile_image.fill(color)
                    screen.blit(tile_image, (x, y))
                    pygame.draw.rect(screen, (200, 200, 200), (x, y, tile_size, tile_size), 1)
                    if text:
                        to_write = font.render(f"{text}", True, (0, 0, 0))
                        text_rect = to_write.get_rect(center=(x + tile_size // 2, y + tile_size // 2))
                        screen.blit(to_write, text_rect)

            pygame.display.update()
            
            if record: # pictures folder needs to be created
                frame_filename = f"/Users/lucasvilsen/Desktop/AI-FunProjects/Pathfinding  Algorithms/pictures/pictures{i}/frame_{frame_count:04d}.png"
                pygame.image.save(screen, frame_filename)

            node_to_try = solver.one_step(grid=grid)
            if isinstance(node_to_try, list): 
                color_path(node_to_try, grid) 
                print(f"I ({solver.__class__.__name__}) have found a path {len(node_to_try)} moves.")
            elif node_to_try: grid = color_node(node_to_try, grid)
            # time.sleep(0.1)
            frame_count += 1

    pygame.quit()
