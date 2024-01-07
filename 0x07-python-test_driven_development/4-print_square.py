#!/usr/bin/python3

def print_square(size):
    """Prints a square made of '#' characters.

    Args:
        size (int): The size of the square's sides.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        result = ("#" * size)
        print(result)
