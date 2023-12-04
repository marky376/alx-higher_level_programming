#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = a2 = 0
    b1 = b2 = 0

    if len(tuple_a) >= 1:
        a1 += tuple_a[0]

    if len(tuple_a) >= 2:
        a2 += tuple_a[1]

    if len(tuple_b) >= 1:
        b1 += tuple_b[0]

    if len(tuple_b) >= 2:
        b2 += tuple_b[1]

    return a1 + b1, a2 + b2
