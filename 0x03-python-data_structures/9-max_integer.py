#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    i = 1
    max_num = my_list[0]
    while i < length:
        if max_num < my_list[i]:
            max_num = my_list[i]
        i += 1
    return max_num
