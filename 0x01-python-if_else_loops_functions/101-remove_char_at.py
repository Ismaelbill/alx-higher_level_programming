#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    for i in str:
        newStr += i
    if n < 0:
        return newStr
    return newStr[:n] + newStr[n+1:]
