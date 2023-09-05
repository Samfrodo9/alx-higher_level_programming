#!/usr/bin/python3

"""A Module that divides a Matrix"""


def matrix_divided(matrix, div):
    """A function that divides a Matrix by div"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    divided_list = []
    for a_list in matrix:
        if not isinstance(a_list, list):
            raise TypeError("matrix must be a matrix(list of lists) of \
                    integers/floats")
        row = 0
        store = []
        for number in a_list:
            if not isinstance(number, (int, float)):
                raise TypeError("matrix must be a matrix(list of lists) of \
                        integers/floats")
            store.append(round(number/div, 2))
            row += 1
        # Not yet implemented checking for rows
        divided_list.append(store)
        check = row
        double_check = row
    return divided_list
