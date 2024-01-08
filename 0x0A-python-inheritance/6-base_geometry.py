#!/usr/bin/python3
"""module improve Geometry"""


class BaseGeometry:
    """raises an Exception with the message area() is not implemented"""
    def area(self):
        """raise Exception area() is not implemented"""
        raise Exception("area() is not implemented")
