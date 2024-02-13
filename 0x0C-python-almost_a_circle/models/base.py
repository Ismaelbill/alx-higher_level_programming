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

    @staticmethod
    def from_json_string(json_string):
        """ list of json string """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Square:
            instance = cls(dictionary['size'])
        elif cls == Rectangle:
            instance = cls(dictionary['width'], dictionary['height'])
        instance.update(**dictionary)
        return instance
