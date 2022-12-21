#!/usr/bin/python3
"""a square class"""


class Square:
    """with its methods"""
    def __init__(self, size=0):
        """constructor method"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):

        """return area"""

        return (self.__size ** 2)
