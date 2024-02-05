#!/usr/bin/python3
""" MODULE """


def is_same_class(obj, a_class):
    """
        function return True if the object is exactly an instance
        of a_class, otherwise False
    """
    return (type(obj) is a_class)
