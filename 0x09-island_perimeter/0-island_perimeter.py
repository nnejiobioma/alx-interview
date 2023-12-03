#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ perimeter of the island described in grid """
    perimeter = 0

    for s, row in enumerate(grid):
        for k, element in enumerate(row):
            # Element is land or sea check
            if (element == 0):
                continue

            # Left check
            if (k != 0 and row[k - 1] == 0):
                perimeter += 1
            if (k == 0):
                # left
                perimeter += 1

            # Right check
            if (k != len(row) - 1 and row[k + 1] == 0):
                perimeter += 1
            if (k == len(row) - 1):
                # right
                perimeter += 1

            # Upper check
            if (s != 0 and grid[s - 1][k] == 0):
                perimeter += 1
            if (s == 0):
                # top
                perimeter += 1

            # Bottom Check
            if (s != len(grid) - 1 and grid[s + 1][k] == 0):
                perimeter += 1
            if (s == len(grid) - 1):
                # bottom
                perimeter += 1

    return perimeter
