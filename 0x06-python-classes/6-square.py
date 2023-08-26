#!/usr/bin/python3
'''A module for working with squares.
'''


class Square:
    '''Represents a 2D Polygon with 4 equal and perpendicular sides.
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initializes a Square with a given size.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Retrieves the size of this Square.

        Returns:
            int: The size of this Square.
        '''
        return self.__size

    @property
    def position(self):
        '''Retrieves the position of this Square.

        Returns:
            tuple: The position of this Square.
        '''
        return self.__position

    @size.setter
    def size(self, value):
        '''Updates the size of this Square.

        Args:
            value (int): The new size of this Square.
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    @position.setter
    def position(self, value):
        '''Updates the position of this Square.

        Args:
            value (tuple): The new position of this Square.
        '''
        is_invalid_value = True
        error_msg = 'position must be a tuple of 2 positive integers'
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        is_invalid_value = False
        if is_invalid_value:
            raise TypeError(error_msg)
        else:
            self.__position = value

    def area(self):
        '''Computes the area of this Square.

        Returns:
            int: The area of this Square.
        '''
        return self.size ** 2

    def my_print(self):
        '''Prints a 2D table of the '#' symbol with the size of this square
        based on its position.
        '''
        if self.size == 0:
            print('')
        else:
            print('{}'.format('\n' * self.position[1]), end='')
            for i in range(self.size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.size))
