#!/usr/bin/python3
""" A class module. """


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

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dict = dict()
            old_dict = self.__dict__
            for (key, value) in old_dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
