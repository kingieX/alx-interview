#!/usr/bin/python3
"""
2D matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise

    Args:
        matrix (list): n x n. Matrix to rotate
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[j][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
