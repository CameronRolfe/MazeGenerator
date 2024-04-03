# Maze(num_rows, num_cols, start_row = 0, start_col = 0, end_row = None, end_col = None, seed = None)
When initalized, a maze is automatically generated. 

The generated maze can be accesed, viewed and exported in many ways using Maze and MazeVisualizer.

## Grid
The maze is represented by a 2D grid of cells, where each cell initally has 4 walls (the walls between neighbour cells are shared).

To account for the cell walls, the generated maze will have ((2 x number of rows) + 1) rows and ((2 x number of cols) + 1) columns

For example, a Maze that is created with the arguments num_rows=40 and num_cols=60 will generate a maze that is represented with 81 rows and 121 columns

Maze has two properties **Maze.grid** and **Maze.grid_solution**

Both of these are representations of the generated Maze in the form of a 2D list of numbers where each number corresponds to a cell type

| Cell Type | Description                                                  
| ---        |    ----                                                     
| 0          | Walkable Cell                                                  
| 1          | Wall                                        
| 2          | Start Cell
| 3          | End Cell
| 4          | Solution Path

**Maze.grid_solution** Replaces the 0s representing the solution path in **Maze.grid** with 4s

# Examples
```python
from CamsMazes.maze import Maze
# Some examples of mazes

# Create Maze with minimum arguments
maze = Maze(num_rows=40, num_cols=40)

# Starts generatring maze at (5, 10). End cell is set to (25, 15)
maze_2 = Maze(num_rows=60, num_cols=40, start_row=5, start_col=10, end_row=25, end_col=15) 

# If seed is provided, the seed is used to generate the maze
maze_3 = Maze(num_rows=60, num_cols=60, seed="test seed")
```

# Functions
## to_image(file_name="maze", cell_size=15, show_solution=False)
Exports png of Maze. When solution is True image will contain solution
```python
from CamsMazes.maze import Maze
maze = Maze(num_rows=40, num_cols=40)
maze.to_image() # Creates maze.png
maze.to_image(file_name="maze_solution", show_solution=True) # Creates maze_solution.png (Image includes solution)
```

## to_gif(file_name = "maze", cell_size=10)
Exports gif of maze generation
```python
from CamsMazes.maze import Maze
maze = Maze(num_rows=40, num_cols=40)
maze.to_gif() # Creates maze.gif
maze.to_gif(file_name="maze_2", cell_size=15) # Creates maze_2.gif. Each cell is 15 pixels x 15 pixels
```

## to_txt(file_name="maze", show_solution=False)
Exports maze to txt file
```python
from CamsMazes.maze import Maze

# Examples of to_txt
maze = Maze(num_rows=40, num_cols=40)
maze.to_txt() # Create maze.txt
maze.to_txt(file_Name="maze_sol", show_solution=True) # Creates maze_sol.txt (txt will be populated with solution)
```

## to_json()
Returns json representation of Maze in the following format
```json
{
    "numRows": Maze.num_rows,
    "numCols": Maze.num_cols,
    "startRow": Maze.start_row,
    "startCol": Maze.start_col,
    "endRow": Maze.end_row,
    "endCol": Maze.end_col,
    "seed": Maze.seed,
    "grid": {
        "rows": Maze.grid_rows,
        "cols": Maze.grid_cols,
        "startCell": Maze.start_grid_cell,
        "endCell": Maze.end_grid_cell, 
        "maze": Maze.grid,
        "mazeSolution": Maze.grid_solution,
        "generationPath": Maze.generation_path,
        "solutionPath":  Maze.solution
    }
}

```
## print(show_solution=False)
Prints maze to console
```python
from CamsMazes.maze import Maze
maze = Maze(num_rows=20, num_cols=20, seed="test seed")
maze.print()
print(maze) # This also works and is equivalent to maze.print()
```
Output
```
#########################################
#S  #     #             #           #   #
### # # # ####### ####### ##### ### # # #
#   # # #   #   #       #   #   #   # # #
# ##### ### # # ##### # ### # ### ##### #
# #   # # #   #     # #     # # #       #
# # # # # ######### ### ##### # ####### #
# # #   #         #   # #   # #     #   #
# # ##### ####### ### ### # # # # ### ###
#   #       # #     #   # #   # # #   # #
####### ### # # ####### # ##### # # ### #
#     #   # # # # #     #   #   # # #   #
# ### ##### # # # # ####### # ### # # # #
# # #     # #   # # #       #   # # # # #
# # ##### # # ### # # ########### # # # #
# #     #   #     # #   #         #   # #
# ##### ### ####### # # # ### # ####### #
# #   #     #     # # # #   # # #       #
# # # ### ### ### # # # ##### ### #######
#   #   # # # # # # # #     # #   #   # #
# ##### # # # # # # ####### # # ### # # #
# #     #   # # # #         # # #   #   #
### # ##### # # # ########### # ### #####
#   # #   # #   #         #   #   #     #
# ##### # # ### ####### # # ##### # ### #
# #     # # # #       # # #   #   #   # #
# # ##### # # ### ##### # # # # ####### #
# # #   # # #   # #   # # # # # #       #
# # # # # # # ### # # # # ### # ### ### #
#   # # # #   #   # # # #     #     #   #
# ### # # ##### ### # # ##### ####### ###
#     # # #       # #   #       # #   # #
####### # # ####### ########### # # ### #
#       #   # #     #         #   #     #
# ########### # ##### ####### ######### #
#     #       #     #   #   #       #   #
##### ####### ##### ### # # ##### ### ###
#     #     #   #   #   # #   # # #   # #
# ##### ### # # # ### ##### # # # # ### #
#       #     # #           #   #      E#
#########################################
```
```python
from CamsMazes.maze import Maze
maze = Maze(num_rows=20, num_cols=20, seed="test seed")
maze.print(show_solution=True)
```
Output when show_solution is True
```
#########################################
#SXX#  XXX#             #      XXXXX#   #
###X# #X#X####### ####### #####X###X# # #
#XXX# #X#XXX#XXX#       #   #XXX#XXX# # #
#X#####X###X#X#X##### # ### #X###X##### #
#X#XXX#X# #XXX#XXXXX# #     #X# #XXXXXXX#
#X#X#X#X# #########X### #####X# #######X#
#X#X#XXX#         #XXX# #XXX#X#     #XXX#
#X#X##### ####### ###X###X#X#X# # ###X###
#XXX#       # #     #XXX#X#XXX# # #XXX# #
####### ### # # #######X#X##### # #X### #
#     #   # # # # #XXXXX#XXX#   # #X#XXX#
# ### ##### # # # #X#######X# ### #X#X#X#
# # #     # #   # #X#XXXXXXX#   # #X#X#X#
# # ##### # # ### #X#X########### #X#X#X#
# #     #   #     #X#XXX#         #XXX#X#
# ##### ### #######X# #X# ### # #######X#
# #   #     #     #X# #X#   # # #XXXXXXX#
# # # ### ### ### #X# #X##### ###X#######
#   #   # # # # # #X# #XXXXX# #XXX#   # #
# ##### # # # # # #X#######X# #X### # # #
# #     #   # # # #XXXXXXXXX# #X#   #   #
### # ##### # # # ########### #X### #####
#   # #   # #   #         #   #XXX#     #
# ##### # # ### ####### # # #####X# ### #
# #     # # # #       # # #   #XXX#   # #
# # ##### # # ### ##### # # # #X####### #
# # #   # # #   # #   # # # # #X#  XXXXX#
# # # # # # # ### # # # # ### #X###X###X#
#   # # # #   #   # # # #     #XXXXX#XXX#
# ### # # ##### ### # # ##### #######X###
#     # # #       # #   #       # #XXX# #
####### # # ####### ########### # #X### #
#       #   # #     #         #   #XXXXX#
# ########### # ##### ####### #########X#
#     #       #     #   #   #       #XXX#
##### ####### ##### ### # # ##### ###X###
#     #     #   #   #   # #   # # #XXX# #
# ##### ### # # # ### ##### # # # #X### #
#       #     # #           #   #  XXXXE#
#########################################
```

## generate_maze()
Used to generate new maze.