#!/usr/bin/python3
"""  Load, add, save """


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fileName = 'add_item.json'
args = sys.argv[1:]
i = 0

if os.path.exists(fileName):
    x = load_from_json_file(fileName)
    while i < len(args):
        x.append(args[i])
        i += 1
    save_to_json_file(x, fileName)
else:
    save_to_json_file(args, fileName)
