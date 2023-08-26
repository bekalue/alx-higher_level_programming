#!/usr/bin/python3
"""
a module with `BaseGeometry` class
"""


class BaseGeometry(object):
    """
    The base class for all geometry objects.
    """

    def area(self):
        """
        Computes the area of this geometry.

        Raises:
             Exception: an area is not implemeted.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates an object expected to be a positive and
        non-zero integer object.

        Args:
            name (str): The name of the integer value.
            value (int): The object to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less zero.
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
