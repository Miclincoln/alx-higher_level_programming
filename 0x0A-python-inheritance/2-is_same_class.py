#!/usr/bin/python3

""" A function module. """


def is_same_class(obj, a_class):

    """
    Definition of class "is_same_class"

    Args:
       obj: An object
       a_class: A class.

    Return:
         Return True if "obj" is an instance of "a_class".
    """

    return type(obj) == a_class
