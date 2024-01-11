#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    summ = 0
    div = 0
    for i in my_list:
        summ += (list(i)[0] * list(i)[1])
        div += list(i)[1]
    return summ / div
