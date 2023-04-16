#!/usr/bin/python3

"""A module that defines a triangle"""


class Rectangle:
    """ Definition of a class "Triangle"."""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculate the area of a rectangle.

        Return:
              Returns the area of a rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculates the perimeter of a rectangle.

        Return:
              Returns the perimeter of a rectangle.
        """
        if(self.__height == 0 or self.__width == 0):
            return 0
        else:
            return 2*(self.__height + self.__width)

    def __str__(self):
        """ String representation of a rectangle """
        string_rec = ""
        if(self.__height == 0 or self.__width == 0):
            return string_rec
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string_rec += str(self.print_symbol)

                if i < self.__height - 1:
                    string_rec += "\n"
            return string_rec

    def __repr__(self):
        """ String representation of the rectangle to receate new instance. """
        return "Rectangle ({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ When deleting an instance. """
        Rectangle.number_of_instances -= 1  # decreases the instances by one
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rect with the biggest area.
        Args:
            rect_1 (Rectangle): first instance
            rect_2 (Rectangle): second instance
        Raises:
            TypeError: if any of the parameters is not an instance of
                ``Rectangle``
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @property
    def width(self):
        """``width`` property.
        Args:
            value (int): sets the value of the width variable.
        Raises:
            TypeError: If ``value`` is not an integer.
            ValueError: If ``value`` < 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """``height`` property.
        Args:
            value (int): sets the value of the height variable.
        Raises:
            TypeError: If ``value`` is not an integer.
            ValueError: If ``value`` < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Calculates and returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
