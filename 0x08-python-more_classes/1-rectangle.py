#!/usr/bin/python3
""" define a rectangle class."""

class Rectangle:
    """ define ractangle."""

    def __init__(self, width=0, height=0):
        """ Initializes a new Rectangle instance.

        Args:
        width (int): the width of the rect.
        height (int): the height of the rect.

        """
        self.width = width
        self.height = height

    def width(self):
        """getter method for width"""
        return self.__width

    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Getter method for height."""
        return self.__height

    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
