#!/usr/bin/python3

""" A function module """


def inherits_from(obj, a_class):

    """
    Definition of the function ``inherits_from``.

    args:
       obj: First parameter, an object
       a_class: Second parameter, a class.

    Return:
          True if ``obj`` is an instance of ``a_class`` else False
    """

    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False
