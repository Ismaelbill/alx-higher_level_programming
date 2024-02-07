#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """ function returns the dictionary of obj """
    return obj.__dict__
