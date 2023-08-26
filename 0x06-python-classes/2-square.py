#!/usr/bin/python3

"""A module that contain Square class
"""


class Square:
    """Represents a 2D polygon with 4 sizes and perpendicular sides
    
    Args:
         size (int): a parameter that intializes ``__size`` private instance attribute
         
    Attributes:
         __size (int): a private intstance attribute.
    
    Raises:
         TypeError: if ``__size`` attribute is not integer type.
         ValueError: if ``__size`` attribute is less than zero.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
