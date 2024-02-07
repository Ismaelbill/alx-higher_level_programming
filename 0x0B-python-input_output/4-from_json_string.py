#!/usr/bin/python3
import json
""" from json string to object """


def from_json_string(my_str):
    """ function returns an object """
    return json.loads(my_str)
