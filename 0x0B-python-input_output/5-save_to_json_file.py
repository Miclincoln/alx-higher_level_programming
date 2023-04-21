#!/usr/bin/python3
""" A module that writes an object to a text file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """
    Definition of the function ``save_to_json_file``.

    args:
        my_obj (Object): First parameter, an object to write to text file.
        filename (string): Second parameter, a text file to write to a file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
