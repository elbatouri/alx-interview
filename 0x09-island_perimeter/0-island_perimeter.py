#!/usr/bin/python3
"""
Returns the perimeter of the island described in the grid.
:param my_grid: 2D list representing the land and water arrangement.
:return: The perimeter of the island.
"""
def island_perimeter(my_grid):
    perimeter = 0
    rows = len(my_grid)
    cols = len(my_grid[0])
    for i in range(rows):
        for j in range(cols):
            if my_grid[i][j] == 1:
                perimeter += 4
                if i > 0 and my_grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and my_grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
