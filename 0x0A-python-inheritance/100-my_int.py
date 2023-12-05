#!/usr/bin/python3
"""Module with a class Myint"""

class MyInt(int):
    """A class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Override the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator."""
        return super().__eq__(other)
