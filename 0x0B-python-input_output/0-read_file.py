#!/usr/bin/python3

""" A function module."""



def read_file(filename=""):
    """ Definition of ``read_file`` function. """

    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            print(line, end="")
