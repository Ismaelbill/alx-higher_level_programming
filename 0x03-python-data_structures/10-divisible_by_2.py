#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    arr = my_list[:]
    n = 0
    for i in my_list:
        if i % 2 == 0:
            arr[n] = True
        else:
            arr[n] = False
        n += 1
    return arr
