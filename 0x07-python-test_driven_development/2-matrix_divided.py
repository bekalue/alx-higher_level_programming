#!/usr/bin/python3
"""
A module that contains Divide a matrix function.
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix
    and returns new list containg the result of each.


    Args:
        matrix (List): The matrix whose elements are to be divided.
        div (int): The number to use as a divisor.
    Returns:
         List: A new list consiting of the result of dividing each element
        in the given matrix by div.

    Raises:
         TypeError: if matrix is not a list of lists of integers or floats
                    and if each row of the matrix are not of the same size.

                    For div, if div is not an integer or float.
         ZeroDivisionError: if div is equal to 0.

    """

    ErrorMessages = (
            'matrix must be a matrix (list of lists) of integers/floats',
            'Each row of the matrix must have the same size',
            'div must be a number',
            'division by zero'
            )
    SizeOfEachRow = 0

    if not isinstance(matrix, list):
        raise TypeError(ErrorMessages[0])
    elif len(matrix) == 0:
        raise TypeError(ErrorMessages[1])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(ErrorMessages[0])
        elif len(row) == 0:
            raise TypeError(ErrorMessages[1])
        else:
            if SizeOfEachRow == 0:
                SizeOfEachRow = len(row)
            elif len(row) != SizeOfEachRow:
                raise TypeError(ErrorMessages[1])

            for column in row:
                if not isinstance(column, (int, float)):
                    raise TypeError(ErrorMessages[0])
    if not isinstance(div, (int, float)):
        raise TypeError(ErrorMessages[2])
    elif div == 0:
        raise ZeroDivisionError(ErrorMessages[3])
    else:
        new_matrix = []
        for row in matrix:
            res = list(map(lambda x: round(x / div, 2), row))
            new_matrix.append(res)
        return new_matrix
