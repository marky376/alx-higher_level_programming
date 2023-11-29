#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(
                "{:c}".format(ord(char) - 32)
                if 'a' <= char <= 'z'   
                else char, end="")
    print()
