#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    for i in range(len(text)):
        if text[i] == '.':
            print('\n')
        elif text[i] == '?':
            print('\n')
        elif text[i] == ':':
            print('\n')
        else:
            print(text[i], end='')
    print()
