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
        else:
            diction = {}
            for i in attrs:
                if i == 'first_name':
                    diction['first_name'] = self.first_name
                if i == 'last_name':
                    diction['last_name'] = self.last_name
                if i == 'age':
                    diction['age'] = self.age
            return diction
