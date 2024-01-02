#!/usr/bin/python3
def uppercase(str):
    for i in str:
            l = chr(ord(i) - 32)
            print(l if i.isalpha() and ord(i) >= 97 and ord(i) <= 122 else i, end="")
    print("")
