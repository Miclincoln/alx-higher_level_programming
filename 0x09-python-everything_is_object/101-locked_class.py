#!/usr/bin/python3
""" A module that locks creation of new attribute unless 'first_name'."""


class LockedClass:
    """
    Definition of class "LockedClass".
    Only allow creation of new attribute named first name>
    """
    __slots__ = ["first_name"]
