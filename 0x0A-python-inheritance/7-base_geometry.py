#!/usr/bin/python3
""" Improve Geometry """


class BaseGeometry:
    """ Base Geometry """

    def area(self):
        """ raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ raises exceptions of name and value if they are wrong """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
