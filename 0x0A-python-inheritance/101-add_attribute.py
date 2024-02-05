#!/usr/bin/python3
""" MODULE """


def add_attribute(obj, name, value):
    """ function that a new attribute to an object if possible """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
