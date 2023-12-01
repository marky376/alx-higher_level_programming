#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    total = 0

for i in arguments:
    total += int(i)
print(total)
