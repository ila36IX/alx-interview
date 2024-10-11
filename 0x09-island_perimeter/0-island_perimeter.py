#!/usr/bin/python3
"""Island Perimeter - ALX Interview"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    if not (1 <= rows <= 100) or not (1 <= cols <= 100):
        raise ValueError("Grid dimensions must be between 1 and 100")

    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0 and grid[i][j] != 1:
                raise ValueError("Grid values must be 0 or 1")
            if grid[i][j] == 1:
                perimeter += 4
                # Check left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

    return perimeter
