#!/usr/bin/python3
'''A module for working with geometry.
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Represents a Square geometry object.
    '''
    def __init__(self, size):
        '''Initializes a new Square geometry
        object with the given size.

        Args:
            size (int): The size of the square.
        '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Computes the area of this geometry.

        Returns:
            int: The area of this geometry object.
        '''
        return self.__size * self.__size
