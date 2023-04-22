#!/usr/bin/python3
"""
returns a list of lists of integers representing pascal triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    row = [1]

    result = [row]

    for i in range(1, n):
        row = [x+y for x,y in zip(row + [0], [0] + row)]
        result.append(row)

    return result
