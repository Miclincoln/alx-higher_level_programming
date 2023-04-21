#!/usr/bin/python3
""" A module that returns an object representation by JSON string"""
import json


def from_json_string(my_string):
    """
    Definition of the function ``from_json_string``.

    args:
      my_string (string): A string json whose representation is to be returned.

    var:
       json_string: Stores json representation of a string ``my_string``.

    return:
       json_string
    """
    json_string = json.loads(my_string)
    return json_string
