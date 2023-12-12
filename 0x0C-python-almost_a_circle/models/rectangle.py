#!/usr/bin/python3
"""Module for Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """A Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor.

        Args:
            width (int): Width of rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle.
            y (int): y-coordinate of the rectangle.
            id (int): Identifier for the rectangle instance with None as def.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_integer("width", value, False)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_integer("height", value, False)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x-coordinate."""
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y-coordinate."""
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, name, value, allow_zero=True):
        """Method for validating the value as an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not allow_zero and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_positive(self, name, value):
        """Method for validating that the value is positive (> 0)."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_non_negative(self, name, value):
        """Method for validating that the value is non-negative (>= 0)."""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Compute the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            args (int): arguments to send a non-keyworded variable
                length argument list to the function
            kwargs (dict): keyworded variable length of arguments
        """
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }                
