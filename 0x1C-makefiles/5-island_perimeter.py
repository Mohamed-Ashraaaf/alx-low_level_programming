#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (list[list[int]]): A list of lists representing the grid.

    Returns:
        int: The perimeter of the island.

    """
    if not grid:
        return 0

    peri = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                peri += 4

                if i > 0 and grid[i - 1][j] == 1:
                    peri -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    peri -= 2

    return peri
