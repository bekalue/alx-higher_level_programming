#!/usr/bin/python3
"""Contains classes for working with Polygons.
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a polygon with 4 perpendicular and
    equal sides.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new square object.
        Args:
            size (int): The width and height of this square.
            x (int): The horizontal position of this square.
            y (int): The vertical position of this square.
            id (int): The id of this square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Creates a string representation of this polygon.

        Returns:
            str: A string representation of this polygon.
        """
        return '[Square] ({}) {:d}/{:d} - {:d}'.format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets or sets the size of this square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Gets or sets the size of this square.
        """
        self.width = value
        self.height = value
