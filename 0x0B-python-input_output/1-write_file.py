#!/usr/bin/python3

""" A function module to write content to a file. """


def write_file(filename="", text=""):
    """
    Definition of the function ``write_file``.

    args:
        filename (string): First paramemeter, file to write to.
        text (string): Second parameter, text to be written to the file.

    var:
       count: Initiated to indicate the number of charcater in the string.

    return:
          returns ``count`` the number of strings in the text.
    """
    count = 0
    with open(filename, mode='w', encoding='utf-8') as file1:
        count = file1.write(text)
    return count
