#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        for idx, n in enumerate(i):
            if idx < len(i) - 1:
                print("{:d}".format(n), end=" ")
            else:
                print("{:d}".format(n), end="")
        print()
