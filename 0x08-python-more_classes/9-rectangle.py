#!/usr/bin/python3
""" MODULE """


class Rectangle:
    """ Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            return ''
        result = ''
        for i in range(self.__height):
            result += (('#' * self.__width) + '\n')
        return result[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ')'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ instantiate a new square """

        return Rectangle(size, size)
