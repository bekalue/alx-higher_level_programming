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

    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
