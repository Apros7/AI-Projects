import pygame
import numpy as np
import time
import copy

from BaselineSolvers import RandomBaselineSolver, CircleBaselineSolver
from A_star import AstarSolver

pygame.init()

# Setup:
record = True
tile_size = 30
number_tiles_horizontal = 30
number_tiles_vertical = 20
width = tile_size * number_tiles_horizontal
height = tile_size * number_tiles_vertical
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 15)

# colors:
grid = np.random.choice([0, 1], size=(number_tiles_vertical, number_tiles_horizontal), p=[0.75, 0.25])
colors_and_text = [
    ((255, 255, 255), None),    # normal block
    ((0,0,0), None),            # black, blocking block
    ((0,255,0), "Start"),       # start block
    ((30,144,255), "End"),      # end block
    ((255,215,0), None),        # tiles the algorithms has been on
    ((255,105,180), None)]      # the final path

# begin and end point:
begin_point = (np.random.choice(range(number_tiles_vertical)), np.random.choice(range(number_tiles_horizontal)))
end_point = (np.random.choice(range(number_tiles_vertical)), np.random.choice(range(number_tiles_horizontal)))
grid[begin_point[0], begin_point[1]] = 2
grid[end_point[0], end_point[1]] = 3

grid0 = copy.deepcopy(grid)

def color_node(node, grid):
    grid[node[0], node[1]] = 4
    return grid

random_solver = RandomBaselineSolver(start_node=begin_point, target_node=end_point, 
                                cols=number_tiles_horizontal, rows=number_tiles_vertical)
circle_solver = CircleBaselineSolver(start_node=begin_point, target_node=end_point, 
                                cols=number_tiles_horizontal, rows=number_tiles_vertical)
a_star_solver = AstarSolver(start_node=begin_point, target_node=end_point, 
                                cols=number_tiles_horizontal, rows=number_tiles_vertical)

solvers = [random_solver, circle_solver, a_star_solver]

# Main loop

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
            frame_filename = f"pictures{i}/frame_{frame_count:04d}.png"
            pygame.image.save(screen, frame_filename)

        node_to_try = solver.one_step(grid=grid)
        if node_to_try: grid = color_node(node_to_try, grid)
        time.sleep(0.01)
        frame_count += 1

pygame.quit()
