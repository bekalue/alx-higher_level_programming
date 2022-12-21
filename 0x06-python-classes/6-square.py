#!/usr/bin/python3
"""a class modulE"""


class Square:

    def __init__(self, value=0, position=(0, 0)):
        """initializer"""
        self.__size = value
        self.__position = position

    @property
    def size(self):
        """size retriver"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        self.__size == value
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def position(self):
        """postion retriver"""
        return self.__position

    @position.setter
    def position(self, value):
        """postion setter"""
        self.__position = value
        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(self.__position[0]) != int or \
                type(self.__position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif self.__position[0] < 0 or self.__postion[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """return area"""
        return (self.__size ** 2)

    def my_print(self):
        """print"""
        if self.__size > 0:
            if self.__position[1] > 0:
                for newline in range(self.__position[1]):
                    print()
            for row in range(self.__size):
                if self.__position[0] > 0:
                    for spaces in range(self.__position[0]):
                        print("_", end="")
                for collumn in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
