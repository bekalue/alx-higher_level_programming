#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = a2 = b3 = b4 = 0

    try:
        a1 = tuple_a[0]
    except IndexError:
        a1 = 0
    try:
        a2 = tuple_a[1]
    except IndexError:
        a2 = 0
    try:
        b1 = tuple_b[0]
    except IndexError:
        b1 = 0
    try:
        b2 = tuple_b[1]
    except IndexError:
        b2 = 0

    result = (a1 + b1, a2 + b2)
    return result
