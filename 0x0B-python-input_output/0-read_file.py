#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ function that reads a test file and prints it """
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
