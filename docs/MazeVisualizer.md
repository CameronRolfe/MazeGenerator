# MazeVisualizer(maze, cell_size=15, delay_ms=5)
| Parameter  | Description                                                   | Default Value|
| ---        |    ----                                                       |     ---      |
| maze       | Instance of Maze class                                        | **Required** |
| cell_size  | Cell Size in Pixels                                           | 15           |
| delay_ms   | Milliseconds to wait after each maze update during generation | 5            |


## Examples
```python
import Maze from src.Maze
import MazeVisualizer fromn src.MazeVisualizer

# Must first create Maze
maze = Maze(num_rows=40, num_cols=40)

# MazeVisualizer must be created with Maze
maze_visualizer=MazeVisualizer(maze) # GUI will automatically open and maze generation simulation will begin

# Setting cell size
maze_visualizer_2=MazeVisualizer(maze, cell_size=10) # Each cell in maze will be 10 pixels x 10 pixels

# Setting Delay
maze_visualizer_3=MazeVisualizer(maze, delay_ms=1) # Delay (in milliseconds) between each maze update during maze generation
```
## Example GUI Output