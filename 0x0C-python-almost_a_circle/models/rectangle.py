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
        """ function that validate setter methods """
        if type(var) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not value and var <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif value and var < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """ returns the area value """
        return self.width * self.height

    def display(self):
        """ prints in stdout character '#' """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """ returns a string representation for instances of cls """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def edit_update(self, id=None, width=None, height=None, x=None, y=None):
        """ assigning method """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ no-keyword argument public method """
        if args:
            self.edit_update(*args)
        elif kwargs:
            self.edit_update(**kwargs)

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id,
            'height': self.height, 'width': self.width}
