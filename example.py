from src.Maze import Maze
from src.MazeVisualizer import MazeVisualizer

# How to use Maze

# Create Maze with minimum arguments
maze = Maze(num_rows=40, num_cols=40)
# Starts generatring maze at (5, 10). End cell is set to (25, 15)
maze_2 = Maze(num_rows=60, num_cols=40, start_row=5, start_col=10, end_row=25, end_col=15) 
# If seed is provided, the seed is used to generate the maze
maze_3 = Maze(num_rows=20, num_cols=20, seed="test seed")

# How to use MazeVisualizer

# Create MazeVisualizer with minimum arguments
maze_visualizer = MazeVisualizer(maze) # Opens GUI and the maze generation can be viewed

maze_visualizer2 = MazeVisualizer(maze_2, cell_size=10) # Each cell in maze is cell_size pixels by cell_size pixels

maze_visualizer3 = MazeVisualizer(maze_3, cell_size=10, delay_ms=2) # Delay (in milliseconds) between each maze update during maze generation