#!/usr/bin/python3

"""module for __eq__(==) and __ne__(!=)"""


class MyInt(int):
    """class for __eq__ and __ne__"""
    def __eq__(self, other):
        """method for equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """method for not equal"""
        return super().__eq__(other)
