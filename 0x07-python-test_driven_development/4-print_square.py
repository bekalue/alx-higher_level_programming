#!/usr/bin/python3
"""
A module that contains one function
"""


def print_square(size):
    """
    a a function that prints a square with the character #

    Args:
         size (int): the size of the square.

    Raises:
         TypeError: if size is not integer and less than zero.
         ValueError: if size is integer and less than zero.
    """

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    elif not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            print('{}'.format('#' * size))
