#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = set(my_list)
    sum = 0
    for i in x:
        sum += i
    return sum
