#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """ determines of the object is an instance of a class that inhertited """
    return (isinstance(obj, a_class) and type(obj) is not a_class)
