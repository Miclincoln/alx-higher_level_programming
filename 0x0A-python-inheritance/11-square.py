#!/usr/bin/python3
""" A class module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Definition of calss ``Square``"""
    def __init__(self, size):
        """ Initializing class ``Square``"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size
