#!/usr/bin/python3
""" MODULE """


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ property to retrieve it """
        return self.__width

    @width.setter
    def width(self, value):
        """ property setter to set it """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ property to retrieve it """
        return self.__height

    @height.setter
    def height(self, value):
        """ property setter to set it """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ print the rectangle with the character # """

        if self.__height == 0 or self.__width == 0:
            return '\n'
        result = ''
        for i in range(self.__height):
            for x in range(self.__width):
                result += '#'
            result += '\n'
        return result[:-1]
