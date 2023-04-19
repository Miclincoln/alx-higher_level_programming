#!/usr/bin/python3

""" A function module"""


def is_kind_of_class(obj, a_class):

    """
    Definition of function ``is_kind_of_class``.

    args:
        obj: First parameter, an object
        a_class: Second parameter, a class.

    return:
        Returns True if ``obj`` is an instance of ``a_class`` or inherit from.
    """

    return isinstance(obj, a_class)
