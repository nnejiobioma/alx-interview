#!/usr/bin/python3
""" This rotate 2D matrix module.
"""


def rotate_2d_matrix(matrix):
    """Rotate it 90 degrees clockwise.
    """

    c = matrix.copy()

    for iter in range(len(matrix[0])):
        aux = []
        for row in reversed(c):
            aux.append(row[iter])
        matrix[iter] = aux
