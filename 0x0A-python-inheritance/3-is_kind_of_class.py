#!/usr/bin/python3
"""
A module for working with instance of an object.
"""


def is_kind_of_class(obj, a_class):
    """
    A function that checks if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    Args:
        obj (any): an object to be checked.
        a_class (any): A class to be compared against.

    Returns:
         bool: True if `obj` is an instance of `a_class` or any
        of its superclasses.
    """
    return isinstance(obj, a_class)
