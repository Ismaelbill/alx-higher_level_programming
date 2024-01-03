#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    for i in str:
        newStr += i
    return newStr[:n] + newStr[n+1:]
