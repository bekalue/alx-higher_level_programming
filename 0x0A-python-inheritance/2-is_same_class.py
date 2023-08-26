#!/usr/bin/python3
"""
A module for working with insatances of an object.
"""


def is_same_class(obj, a_class):
    """
    A function that checks if the object is exactly
    an instance of the specified class.

    Args:
        obj (any): any type of an object.
        a_class (class): a class name.

    Returns:
         bool: True if obj is exactly an instance of `a_class`.
    """
    return type(obj) is a_class
