#!/usr/bin/python3
import json

""" A module that return JSON representation of a string. """


def to_json_string(my_obj):
    """
    Definition of the function ``to_json_string``.

    args:
       my_obj (string): Object whose json representation is to be returned.

    var:
       json_data: Stores json representation of an object ``my_obj``.

    return:
       json_data
    """
    json_data = json.dumps(my_obj)
    return json_data
