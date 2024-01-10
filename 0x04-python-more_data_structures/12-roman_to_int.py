#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rmn = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500,
        'M': 1000
    }
    rmnstr = roman_string
    i, num, length = 0, 0, len(rmnstr)
    while i < (length):
        if rmnstr[i] in rmn:
            if i + 1 < length and rmn[rmnstr[i]] < rmn[rmnstr[i+1]]:
                num -= rmn[rmnstr[i]]
            else:
                num += rmn[rmnstr[i]]
        i += 1
    return num
