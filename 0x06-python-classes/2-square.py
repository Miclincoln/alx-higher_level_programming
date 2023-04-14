#!/usr/bin/python3

"""
A module that defines a Square by its size
"""


class Square:
    """
    Definition of the class "Square".
    """
    def __init__(self, size=0):
        """
        Initialization of the "Square" class attributes.

       Args:
            Size (int): First parameter, defines the size of the square.
        """
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
