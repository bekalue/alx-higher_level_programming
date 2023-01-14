#!/usr/bin/python3
"""Contains classes for working with Polygons.
"""
from .base import Base


class Rectangle(Base):
    """Represents a polygon with 4 perpendicular and
    two pairs of equal sides.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle object.

        Args:
            width (int): The width of this rectangle.
            height (int): The height of this rectangle.
            x (int): The horizontal position of this rectangle.
            y (int): The vertical position of this rectangle.
            id (int): The id of this rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets or sets the width of this rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Gets or sets the height of this rectangle.
        """
        return self.__height

    @property
    def x(self):
        """Gets or sets the horizontal position of this rectangle.
        """
        return self.__x

    @property
    def y(self):
        """Gets or sets the vertical position of this rectangle.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Gets or sets the width of this rectangle.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Gets or sets the height of this rectangle.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """Gets or sets the horizontal position of this rectangle.
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """Gets or sets the vertical position of this rectangle.
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Computes the area of this rectangle.

        Returns:
            int: The area of this rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints a text representation of this rectangle.
        """
        h_off = ' ' * self.x
        h_val = '#' * self.width
        print('\n' * self.y, end='')
        print('{:s}{:s}\n'.format(h_off, h_val) * self.height, end='')

    def __str__(self):
        """Creates a string representation of this polygon.

        Returns:
            str: A string representation of this polygon.
        """
        parts = (
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )
        res = '[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}'.format(
            parts[0], parts[1], parts[2], parts[3], parts[4]
        )
        return res

    def update(self, *args, **kwargs):
        """Updates the attributes of this polygon.

        Args:
            args (tuple): A tuple of non-keyword arguments.
            kwargs (dict): A dictionary of keyword arguments.
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
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
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return res
