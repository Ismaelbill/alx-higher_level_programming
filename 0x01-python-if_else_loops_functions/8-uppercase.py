#!/usr/bin/python3
def uppercase(str):
    result = ""
    num = ""
    for i in str:
        if i.isalpha() and ord(i) >= 97 and ord(i) <= 122:
            num = chr(ord(i) - 32)
            result += num
        else:
            result += i
    print("{}".format(result))
