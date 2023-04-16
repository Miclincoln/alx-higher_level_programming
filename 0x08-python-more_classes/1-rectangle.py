#!/usr/bin/python3

"""A module that defines a triangle"""


class Rectangle:
    """ Definition of a class "Triangle"."""

    def __init__(self, width=0, height=0):
        """
        Initialization of the class "Rectangle" attributes.

        Args:
            width (int): First argument, the width of the rectangle
            height (int): Second parameter, the width of the triangle.

        Raises:
              ValueError: If width and height is < 0.
              TypeError: If width and height is not an int.
        """

        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
        "width" property.

        Return:
              width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        "width" setter.

        Args:
            value (int): First parameter, takes an int.

        Raises:
            ValueError: If width is < 0.
            TypeError: If width is not an int.
        """
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        'property' height.

        Returns:
            height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        "height" setter.

        Args:
           value (int): First parameter, takes an int.

        Raises:
            ValueError: If height is < 0.
            TypeError: If height is not an int.
        """
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")