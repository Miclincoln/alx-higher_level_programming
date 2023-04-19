#!/usr/bin/python3

""" A class module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Imports class ``BaseGeometry`` for inheritance """


class Rectangle(BaseGeometry):

    """
    Definitition of class ``Rectangle``

    args:
       ``Rectangle`` inherited class
    """

    def __init__(self, width, height):
        """ Inititialization of class ``Rectangle``."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width:d}/{self.__height:d}")
