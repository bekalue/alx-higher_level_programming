#!/usr/bin/python3
"""
A module that contains Rectange class.
"""


class Rectangle:
    """
    A Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a class for an instance

        Args:
           Width (int): the width of the rectangle
           height (int): the hight of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrives the width of the rectangle.

        Returns:
             int: the width of rectangle (private instance variable)
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Updates the width of the rectangle.

        Args:
            value (int): the value that updates the width of the rectangle.

        Raise:
            TypeError: if width is not an integer.
            ValueError: if width is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrives the height of the rectangle.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Updates the height of the rectangle.

        Args:
            value (int): new value for the height of the rectangle

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
