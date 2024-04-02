from src.Maze import Maze
from src.MazeVisualizer import MazeVisualizer
maze = Maze(num_rows=40, num_cols=40, start_col = 0, start_row=0)
maze.to_image()
maze.to_image("maze_sol", showSolution=True)
#maze.to_gif(cell_size=10)
maze_visualizer = MazeVisualizer(maze, delay_ms=0)