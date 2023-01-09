#!/usr/bin/python3
"""
A module for inspecting an object.
"""


def lookup(obj):
    """
    Finds the list of available attributes and methods of an object.

    Args:
        obj (any): any type of object that will
                   be passed for inspection
    Returns:
         list: the list of available attributes and
               methods of an object
    """
    return dir(obj)
