#!/usr/bin/python3
"""
The pascal's triangle
"""


def pascal_triangle(n):
    """
        Function that returns a list
        of lists of integers representing
        the pascal's triangle of n.
    """
    if n <= 0:
        return []
    row = [1]
    result = [row]
    for i in range(1, n):
        row = [x+y for x,y in zip(row + [0], [0] + row)]
        result.append(row)
    return result
