#!/usr/bin/python3
""" First Rectangle """


from models.base import Base


class Rectangle(Base):
    """ class Rectangle
        inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.validation_func("width", val, False)
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.validation_func("height", val, False)
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.validation_func("x", val)
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.validation_func("y", val)
        self.__y = val

    def validation_func(self, name, var, value=True):
        if type(var) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not value and var <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif value and var < 0:
            raise ValueError("{} must be >= 0".format(name))
