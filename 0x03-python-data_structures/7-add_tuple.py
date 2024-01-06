#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b

    if len(a) < 2:
        if len(a) == 0:
            a = (0, 0)
        a += (0, )
    if len(b) < 2:
        if len(b) == 0:
            b = (0, 0)
        b += (0, )
    a = a[:2]
    b = b[:2]

    result = tuple(x + y for x, y in zip(a, b))
    return result
