#!/usr/bin/python3
"""
a module with a class
"""


class BaseGeometry(object):
    """
    a class `BaseGeometry` that have unimplemented area method.

    Raises:
         Exception: prints area is not implemented, if area method is called.
    """

    def area(self):
        raise Exception('area() is not implemented')
