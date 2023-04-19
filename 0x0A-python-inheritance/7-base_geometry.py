#!/usr/bin/python3

""" A class module. """


class BaseGeometry:
    """ Definition of class ``BaseGeometry``."""

    def area(self):

        """
        Definition of public instance method ``area``.

        Raises:
             Exception; area() is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Definition of a public instance method ``integer_validator``

        Raises:
             TypeError: If value is not an integer.
             ValueError: if value is <= 0.
"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
