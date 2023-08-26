#!/usr/bin/python3
""" a module that contain square class
"""


class Square:
    """Representation of 2D polygon with 4 equal and perpendicular sides
    
    Args:
        size (int): attribute intializer parameter
    Attributes:
        __size (int): a private instance attribute.
    """

    def __init__(self, size=0):
        """intializer
        """
        self.__size = size

    @property
    def size(self):
        """size retriver
        
        Returns:
             int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter(updates square size)
        
        Args:
            Value (int): updates the size of square
        Raises:
            TypeError: if value is not integer type.
            ValueError: if value is less than zero.
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """computes area
        
        Returns:
              int: area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints a 2D table of the '#' symbol with the size of this square.
        """
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
