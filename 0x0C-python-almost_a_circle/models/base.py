#!/usr/bin/python3
""" Base class """


import json


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json representation """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ list of the json string representation """
        if list_objs is None:
            list_objs = []
        a = []
        for obj in list_objs:
            a += [obj.to_dictionary()]
        fileName = cls.__name__ + ".json"
        with open(fileName, "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(a))
