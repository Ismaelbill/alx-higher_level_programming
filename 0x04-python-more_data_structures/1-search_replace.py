#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = my_list[:]
    i = 0
    while i < len(newList):
        if newList[i] == search:
            newList[i] = replace
        i += 1
    return newList
