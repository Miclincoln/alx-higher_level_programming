#!/usr/bin/python3

"""
A module that calculates the Area of a "Square".
"""


class Square:
    """
    Definition of the class "Square".
    """
    def __init__(self, size=0):
        """
        Initialization of the class "Square" attributes.

        Args:
            Size (int): First parameter: Size of the Square.
        """
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueErro("size must be >= 0")

    def area(self):

        """
        Calculates the Area of a Square
        Return:
            Area of Square if successful, 0 if nothing is supllied.
        """

        return self.__size * self.__size
