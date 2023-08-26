#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []

    for i in matrix:
        square_matrix.append(list(x ** 2 for x in i))
    return square_matrix
