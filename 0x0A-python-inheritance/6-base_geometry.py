#!/usr/bin/python3
"""module with class BaseGeometry"""

class BaseGeometry:
    """A class with an area() method that raises an exception."""

    def area(self):
        """Raise an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
