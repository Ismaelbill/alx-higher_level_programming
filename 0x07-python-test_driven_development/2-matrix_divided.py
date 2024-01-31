#!/usr/bin/python3
"""
Dividing A Matrix
"""


def check_int_float(ls):
    for i in ls:
        for x in i:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("matrix must be a matrix (list of\
                        lists) of integers/floats")


def matrix_divided(matrix, div):
    """
    matrix_divided
    """
    ls = [row[:] for row in matrix]
    check_int_float(ls)
    if len(ls[0]) != len(ls[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(ls)):
        for x in range(len(ls[i])):
            ls[i][x] = round(ls[i][x] / div, 2)
    return ls
