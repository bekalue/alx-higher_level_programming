#!/usr/bin/python3
"""a square class"""


class Square:
    """conatins blah blah"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """size retriver"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """area"""
        return (self.__size ** 2)
