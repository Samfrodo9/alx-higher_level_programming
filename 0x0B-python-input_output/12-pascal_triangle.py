#!/usr/bin/python3

"""
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """A function doing the above"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(len(prev_row) - 1):
            new_value = prev_row[i] + prev_row[i + 1]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
