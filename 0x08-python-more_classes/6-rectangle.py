#!/usr/bin/python3
"""
A module for working with rectangles.
"""


class Rectangle:
    """
    A rectangle class

    Attributes:
         number_of_instances (int): holds number of instances created.
    """
    number_of_instances = 0

    @property
    def width(self):
        """
        Retrieves the width of this Rectangle.
        Returns:
            int: The width of this Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height of this Rectangle.
        Returns:
            int: The height of this Rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Updates the width of this Rectangle.
        Args:
            value (int): The new width of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Updates the height of this Rectangle.
        Args:
            value (int): The new height of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """
        Computes the area of this Rectangle.
        Returns:
            int: The area of this Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of this Rectangle.
        Returns:
            int: The perimeter of this Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width * self.height)

    def __repr__(self):
        """
        Returns a representation of this Rectangle's initialization.
        Returns:
            str: A string representation of this Rectangle's initialization.
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __str__(self):
        """
        Returns a string representation of this Rectangle.
        Returns:
            str: A string representation of this Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            char = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(char)

    def __del__(self):
        """
        Performs some routines after an object is deleted.
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
