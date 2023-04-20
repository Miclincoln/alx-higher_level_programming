#!/usr/bin/python3
""" A function module. """


def read_file(filename=""):
    """
    Definition of the ``read_file`` function.

    args:
        filename (string): First parameter, accepts a string.
    prints:
        Reads the text file to stdout.
    """
    with open('my_file_0.txt', mode='r', encoding='utf-8')as file1:
        for text in file1:
            print(text, end="")
