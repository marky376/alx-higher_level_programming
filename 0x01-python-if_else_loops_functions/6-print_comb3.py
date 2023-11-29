#!/usr/bin/python3
for digit1 in range(9):
    for digit2 in range(digit1 + 1, 10):
        end = ", " if not (digit1 == 8 and digit2 == 9) else ""
    print("{}{}".format(digit1 % 10, digit2 % 10), end=end)
print()
