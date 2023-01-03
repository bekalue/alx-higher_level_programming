#!/usr/bin/python3

class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        else:
            char = list(map(lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(char)
