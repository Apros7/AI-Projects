import imageio
import os

path = "/Users/lucasvilsen/Desktop/AI-FunProjects/Pathfinding  Algorithms/pictures1"
frame_files = sorted(os.listdir(path))

os.chdir(path)
frames = [imageio.imread(filename) for filename in frame_files]

output_gif_path = "/Users/lucasvilsen/Desktop/AI-FunProjects/Pathfinding  Algorithms/recordings/circle_solver.gif"

imageio.mimsave(output_gif_path, frames, duration=0.01)