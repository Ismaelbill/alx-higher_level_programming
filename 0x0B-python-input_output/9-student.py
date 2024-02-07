#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ cls student """
    def __init__(self, first_name, last_name, age):
        """ initialize data student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary representation """
        return self.__dict__
