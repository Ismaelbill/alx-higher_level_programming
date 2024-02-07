#!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """ cls student """
    def __init__(self, first_name, last_name, age):
        """ initialize data student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representation """
        if attrs is None:
            return self.__dict__
