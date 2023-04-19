#!/usr/bin/python3

""" A class module of inheritance"""


class MyList(list):
    """
    Definition of class "MyList".

    Inheritance:
        Inherits from "List".
    """

    def print_sorted(self):

        """ Prints the list in sorted ascending order."""

        print(sorted(self))
