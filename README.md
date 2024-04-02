# About Project
Maze Generator and Solver built using Python

## How to use Maze and MazeVisualizer
Use Maze and MazeVisulizer to open a GUI to view maze generation
```python
import Maze from src.Maze
import MazeVisualizer from src.MazeVisualzier

# How to use Maze

# Create Maze with minimum arguments
maze = Maze(num_rows=40, num_cols=40)
# Starts generatring maze at (5, 10). End cell is set to (25, 15)
maze_2 = Maze(num_rows=60, num_cols=40, start_row=5, start_col=10, end_row=25, end_col=15) 
# If seed is provided, the seed is used to generate the maze
maze_3 = Maze(num_rows=60, num_cols=60, seed="test seed")

# How to use MazeVisualizer

# Create MazeVisualizer with minimum arguments
maze_visualizer = Maze(maze) # Opens GUI and the maze generation can be viewed

maze_visualizer2 = Maze(maze2, cell_size=10) # Each cell in maze is cell_size pixels by cell_size pixels

maze_visualizer3 = Maze(maze3, cell_size=10, delay_ms=2) # Delay (in milliseconds) between each maze update during maze generation
```

## Exporting maze to image
Use Maze.to_image to export maze to png
```python
import Maze from src.Maze
maze = Maze(num_rows=40, num_cols=40)
maze.to_img(file_name="maze") # Creates maze.png
maze.to_img(file_name="maze_solution", solution=True) # Creates maze_solution.png (Image contains solution)
maze.to_img(file_name="maze_2", cell_size=10) # Creates maze_2.png where each cell is 10 pixels by 10 pixels
```

## Exporting maze generation to gif
Use Maze.to_gif to export maze generation to gif
```python
import Maze from src.Maze
maze = Maze(num_rows=40, num_cols=40)
maze.to_gif(file_name="maze") # Creates maze.gif
maze.to_gif(file_name="maze_2", cell_size=10) # Creates maze_2.gif where each cell is 10 pixels by 10 pixels
```

## Exporting maze to txt file
Use Maze.to_txt to export maze to txt
```python
import Maze from src.Maze
maze = Maze(num_rows=40, num_cols=40)
maze.to_txt() # Creates maze.txt
maze.to_txt(file_name="maze_2") # file_name can be supplied
maze.to_txt(solution=True) # Populates txt with solution
```

## Exporting maze to JSON
Use Maze.to_json to export maze generation to gif
```python
import Maze from src.Maze
maze = Maze(num_rows=40, num_cols=40)
json = maze.to_json()
```

## Printing maze to console
Use Maze.print to print maze to console
```python
import Maze from src.Maze
maze = Maze(num_rows=40, num_cols=40)
maze.print()
```

# [Maze](docs/Maze.md)
Exhaustive documentation for Maze

# [MazeVisualizer](docs/MazeVisualizer.md)
Exhaustive documentation for MazeVisualizer