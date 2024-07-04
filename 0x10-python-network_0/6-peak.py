#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    i = 1
    peak = list_of_integers[0]
    # arr = list_of_integers
    if list_of_integers[0] > list_of_integers[1]:
        peak = list_of_integers[0]
    while i < (len(list_of_integers) - 1):
        if list_of_integers[i] > list_of_integers[i - 1] and\
                                list_of_integers[i] > list_of_integers[i + 1]:
            peak = list_of_integers[i]
        i += 1
    if list_of_integers[i] > list_of_integers[i - 1]:
        peak = list_of_integers[i]
    return peak
