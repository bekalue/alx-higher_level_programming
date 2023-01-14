#!/usr/bin/python3
"""Contains classes for working with Polygons.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Represents a polygon with 4 perpendicular and
    equal sides.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square object.

        Args:
            size (int): The width and height of this square.
            x (int): The horizontal position of this square.
            y (int): The vertical position of this square.
            id (int): The id of this square.
        """
        super().__init__(size, size, x, y, id)

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

    def __str__(self):
        """Creates a string representation of this polygon.

        Returns:
            str: A string representation of this polygon.
        """
        parts = (
            self.id,
            self.x,
            self.y,
            self.width
        )
        res = '[Square] ({}) {:d}/{:d} - {:d}'.format(
            parts[0], parts[1], parts[2], parts[3]
        )
        return res

    def update(self, *args, **kwargs):
        """Updates the attributes of this polygon.

        Args:
            args (tuple): A tuple of non-keyword arguments.
            kwargs (dict): A dictionary of keyword arguments.
        """
        attrs = ('id', 'size', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Creates a dictionary representation of this polygon.

        Returns:
            dict: A dictionary representation of this polygon.
        """
        res = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return res
