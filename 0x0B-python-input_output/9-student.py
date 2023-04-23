#!/usr/bin/python3
""" A class module. """
import json


class Student:
    """ Definition of the calss ``Student``."""
    def __init__(self, first_name, last_name, age):
        """
        Initilization of the instances of class ``Student``.

        args:
           first_name (string):First parameter, string as a public instance.
           last_name (string): Second parameter, string as a public instance.
           age (int): Third parameter, stores the age as a public instance.

       Return:
             Returns the dictionary representation of the class ``Student``.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
