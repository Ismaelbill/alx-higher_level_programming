#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copyDict = a_dictionary.copy()
    for key in copyDict:
        val = copyDict[key]
        copyDict[key] = val * 2
    return copyDict
