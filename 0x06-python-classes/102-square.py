#!/usr/bin/python3
"""A module for working with squares.
"""


class Square:
    """Represents a 2D Polygon with 4 equal and perpendicular sides.
    """
    def __init__(self, size=0):
        """Initializes a Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of this Square.

        Returns:
            int: The size of this Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Updates the size of this Square.

        Args:
            value (int): The new size of this Square.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is not greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        """Computes the area of this Square.

        Returns:
            int: The area of this Square.
        """
        return self.size ** 2

    def __eq__(self, value):
        '''Performs an equality comparison check between two Square objects.

        Returns:
            bool: True if the area of the Square objects are
            equal, otherwise False.
        '''
        if isinstance(value, Square):
            return self.area() == value.area()
        else:
            return False

    def __ne__(self, value):
        '''Performs a non-equal comparison check between two Square objects.

        Returns:
            bool: True if the area of the Square objects are
            not equal, otherwise True.
        '''
        if isinstance(value, Square):
            return self.area() != value.area()
        else:
            return True

    def __gt__(self, value):
        '''Performs a greater-than comparison check between two Square objects.

        Returns:
            bool: True if the area of the left Square object is
            greater than the second, otherwise False.

        Raises:
            TypeError: If `value` is not a Square object.
        '''
        if isinstance(value, Square):
            return self.area() > value.area()
        else:
            err_msg = "'>' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __ge__(self, value):
        '''Performs a greater-than-or-equal comparison check between
        two Square objects.

        Returns:
            bool: True if the area of the left Square object is
            greater than or equal to the second, otherwise False.

        Raises:
            TypeError: If `value` is not a Square object.
        '''
        if isinstance(value, Square):
            return self.area() >= value.area()
        else:
            err_msg = "'>=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __lt__(self, value):
        '''Performs a less-than comparison check between two Square objects.

        Returns:
            bool: True if the area of the left Square object is
            less than the second, otherwise False.

        Raises:
            TypeError: If `value` is not a Square object.
        '''
        if isinstance(value, Square):
            return self.area() < value.area()
        else:
            err_msg = "'<' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __le__(self, value):
        '''Performs a less-than-or-equal comparison check between
        two Square objects.

        Returns:
            bool: True if the area of the left Square object is
            less than or equal to the second, otherwise False.

        Raises:
            TypeError: If `value` is not a Square object.
        '''
        if isinstance(value, Square):
            return self.area() <= value.area()
        else:
            err_msg = "'<=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False
