#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if i.isalpha() and ord(i) >= 97 and ord(i) <= 122:
            l = chr(ord(i) - 32)
            result += l
        else:
            result += i
    print("{}".format(result))
