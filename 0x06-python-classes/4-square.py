#!/usr/bin/python3
"""a module that contain square class
"""


class Square:
    """ Represents a 2D polygon with 4 equal and perpendicular sides.
    
    Args:
         size (int): intitializes ``__size`` attribute.
    
    Attributes:
         __size (int): a private instance attribute.
    """

    def __init__(self, size=0):
        """ Initialize the square object
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square.
        
        Returns:
              int: the size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ sets(updates) the size of the square
        
        Args:
             value (int): the new size of the square
        Raises:
             TypeError: if __size is not integer type.
             ValueError: if __size is less than zero.
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Computes the area of the square
        
        Returns:
              int: the area of the square
        """
        return (self.__size ** 2)
