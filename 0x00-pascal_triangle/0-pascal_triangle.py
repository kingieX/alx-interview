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
        """
        generate the next row by appending a 0 to the end of the previous row
        and then adding it element-wise to the previous row shifted 
        one position to the right
        """
        row = [x+y for x,y in zip(row + [0], [0] + row)]
        result.append(row)

    return result
