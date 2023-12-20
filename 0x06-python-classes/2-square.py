#!/usr/bin/python3
"""
Creating a square method

"""

class Square:
    """
    a class created called square
    
    """
    def __init__(self, size = 0):
        """
        Instatiation
        """
        if (type(size) is not int):
            """
            Check if the size is an integer. If not, raise a TypeError
            """
            raise TypeError("size must be an integer")
        elif (size < 0):
            """
            If size is less than 0, raise a ValueError.
            
            """
            raise ValueError("size must be >= 0")
        else:
            """
            If size is valid integer and not less than 0,
            assign it to the private instance attribute
            """

            self.__size = size
