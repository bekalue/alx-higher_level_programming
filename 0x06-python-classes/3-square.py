#!/usr/bin/python3
"""A module that contain square class
"""


class Square:
    """ Represnts a 2D polygon with 4 perpendicular sides
    
    Args:
          size (int): a parameter that intializes private instance attribute called __size.
     
    Attributes:
          __size (int): a private intsance attribute.
    
    Raises:
          TypeError: if __size is not integer type
          ValueError: if __size is less than zero.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):

        """Computes area of the square
        
        Returns:
               int: area of the square
        """

        return (self.__size ** 2)
