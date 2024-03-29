#!/usr/bin/python3
""" Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square cls """

    def __init__(self, size, x=0, y=0, id=None):
        """ cls constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str representation for instances of cls """
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def edit_update(self, id=None, size=None, x=None, y=None):
        """ assigning method """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
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
        """ dict representation of a square """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
