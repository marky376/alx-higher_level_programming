#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number)
    i = n % 10
    print(i, end="")
    return n
