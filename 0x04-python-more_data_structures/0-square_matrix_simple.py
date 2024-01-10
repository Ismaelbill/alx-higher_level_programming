#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newMatrix = matrix[:]
    length = len(newMatrix)
    for i in range(length):
        a = list(map(lambda x: x ** 2, newMatrix[i]))
        newMatrix[i] = a
    return newMatrix
