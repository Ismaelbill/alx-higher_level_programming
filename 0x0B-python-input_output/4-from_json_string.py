#!/usr/bin/python3
""" from json string to object """


import json


def from_json_string(my_str):
    """ function returns an object """
    return json.loads(my_str)
