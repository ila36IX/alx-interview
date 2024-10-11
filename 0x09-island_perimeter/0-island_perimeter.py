#!/usr/bin/python3

def island_perimeter(grid):
    """The island doesn’t have lakes water inside that isn’t connected tothe
    water surrounding the island."""
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with 4 sides for each land cell
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                if i < rows-1 and grid[i+1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                if j < cols-1 and grid[i][j+1] == 1:
                    perimeter -= 1

    return perimeter

grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ]
print(island_perimeter(grid))
