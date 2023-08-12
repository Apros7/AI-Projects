import imageio
import os

gifs_to_make = ["random_solver", "circle_solver", "astar_solver", "adjusted_astar"]

for i, gif_to_make in enumerate(gifs_to_make):
    path = f"/Users/lucasvilsen/Desktop/AI-FunProjects/Pathfinding  Algorithms/pictures/pictures{i}"
    frame_files = sorted(os.listdir(path))
    os.chdir(path)
    frames = [imageio.imread(filename) for filename in frame_files]
    output_gif_path = f"/Users/lucasvilsen/Desktop/AI-FunProjects/Pathfinding  Algorithms/recordings/{gif_to_make}.gif"
    imageio.mimsave(output_gif_path, frames, duration=0.01)