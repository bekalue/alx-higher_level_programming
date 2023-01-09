#!/usr/bin/python3
'''A module for working with geometry.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a geometry object.
    '''
    def __init__(self, width, height):
        '''Initializes a new Rectangle geometry
        object with the given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        '''
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Computes the area of this geometry.
        Returns:
            int: The area of this geometry object.
        '''
        return self.__width * self.__height

    def __str__(self):
        '''Returns a string representation of this geometry.
        Returns:
            str: A string representation of this geometry object.
        '''
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
