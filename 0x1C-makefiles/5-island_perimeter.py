#!/usr/bin/python3
""" Calculates the perimeter of the island described in the grid. """

def island_perimeter(grid):
    """ Calculates the perimeter of the island described in the grid.

    Args:
        A list of lists representing the grid.

    Returns:
        The perimeter of the island. """
    perim = 0
    gl = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            gl.append(grid[i][j])
    for i in range(len(gl)):
        if i < len(gl) - 1 and i > 0:
            if gl[i] == 0 and gl[i + 1] == 1 or gl[i] == 0 and gl[i - 1] == 1:
                perim += 1
    if perim % 2 == 0:
        perim *= 2
    else:
        perim = (perim * 2) - 1
    return perim
