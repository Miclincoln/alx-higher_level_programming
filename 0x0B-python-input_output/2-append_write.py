#!/usr/bin/python3
""" A module of function to return the number of text appended to a file."""


def append_write(filename="", text=""):
    """
    Definition of the function ``append_write``.

    args:
        filename (string): First parameter, file to be written to.
        text (string): Second parameter, text to be written into a file.

   var:
      count (int): Initiated to store and return the number of character.

   return:
        Returns count.
    """
    count = 0
    with open(filename, mode='a', encoding='utf-8') as file:
        count = file.write(text)
    return count
