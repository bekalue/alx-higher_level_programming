#!/usr/bin/python3
"""
A module that contain a simple addition function.
"""


def add_integer(a, b=98):
    """
    A function that does a simple addition and returns the value

    Args:
         a(int, float): the first parameter.
         b(int, float): the second parameter.

    Returns:
         int: return an integer sum of the two passed parameters.

    Raises:
         TypeError: if a and b are not integers or floats
    """

    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    elif type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    else:
        a = int(a)
        b = int(b)
        return (a + b)
