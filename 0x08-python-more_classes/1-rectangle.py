#!/usr/bin/python3
""" MODULE """


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.__height = height
        self.__width = width

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
