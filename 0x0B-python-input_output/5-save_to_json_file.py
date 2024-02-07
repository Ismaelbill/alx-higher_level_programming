#!/usr/bin/python3
import json
""" Save Object to a file """


def save_to_json_file(my_obj, filename):
    """ writing an obj to a file """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
