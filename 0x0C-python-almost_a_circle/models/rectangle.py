#!/usr/bin/python3

from .base import Base

class Rectangle(Base):
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

    @width.setter
    def width(self, value):
        """Gets or sets the width of this rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of this rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Gets or sets the height of this rectangle.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Gets or sets the horizontal position of this rectangle.
        """
        return self.__x
    @x.setter
    def x(self, value):
        """Gets or sets the horizontal position of this rectangle.
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value
    @property
    def y(self):
        """Gets or sets the vertical position of this rectangle.
        """
        return self.__y
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
        return self.height * self.width

    def display(self):
        """Prints a text representation of this rectangle.
        """
        h_off = ' ' * self.x
        h_val = '#' * self.width
        print('\n' * self.y, end='')
        print('{:s}{:s}\n'.format(h_off, h_val) * self.height, end='')

    def __str__(self):
        """
        Creates a string representation of this polygon.

        Returns:
            str: A string representation of this polygon.
        """
        return '[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}'.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """
        Updates the attributes of this polygon.

        Args:
            args (tuple): A tuple of non-keyword arguments.
            kwargs (dict): A dictionary of keyword arguments.
        """

        attributes = ('id', 'width', 'height', 'x', 'y')
        for key, value in zip(attributes, args):
            setattr(self, key, value)
