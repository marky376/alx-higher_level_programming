#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    length = len(argv)

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

if operator == '+':
    d = add(a, b)
elif operator == '-':
    d = sub(a, b)
elif operator == '*':
    d = mul(a, b)
elif operator == '/':
    d = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
print("{} {} {} = {}".format(a, operator, b, d))
