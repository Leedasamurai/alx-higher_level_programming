#!/usr/bin/python3
"""Module with the method lookup"""

def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
