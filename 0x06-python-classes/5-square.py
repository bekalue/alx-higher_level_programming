#!/usr/bin/python3
""" a square class"""


class Square:
    """a class"""

    def __init__(self, size=0):
        """intializer"""
        self.__size = size

    @property
    def size(self):
        """size retriver"""
        return self.__size

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
        """return area"""
        return (self.__size ** 2)

    def my_print(self):
        """ print #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
