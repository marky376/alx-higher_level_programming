#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(c if "c" in locals() else None))
