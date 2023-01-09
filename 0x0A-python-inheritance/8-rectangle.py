#!/usr/bin/python3
"""
a module that imports a base class `BaseGeometry` from 7-base_geometry module
and does some stuff in Rectangle subclass.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a geometry object.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle geometry
        object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
