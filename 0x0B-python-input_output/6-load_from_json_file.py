#!/usr/bin/python3
""" A module that create object from a ``JSON file``. """
import json


def load_from_json_file(filename):
    """
    Definition of the function ``load_from_json_file``.

    args:
        filename (string): A 'JSON file' to create an Object from.
    return:
        JSON file
    """
    with open(filename, mode='r', encoding="utf-8")as file:
        return json.load(file)
