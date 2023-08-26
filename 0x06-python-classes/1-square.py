#!/usr/bin/python3

"""this modul contains Square class"""


class Square:
    """a class Square that defines a square with private instance attribute
    
    Args:
         value (int): a value that initializes ``__size`` attribute
    
    Attributes:
         __size (int): a private instance attribute
                       The size of a square is crucial for a square,
                       many things depend of it (area computation, etc.),
                       so i, as class builder, must control the type and
                       value of this attribute.
                       One way to have the control is to keep it privately.
    """
    def __init__(self, value):
        self.__size = value
