#!/usr/bin/python3
"""Module with class MyList"""

class MyList(list):
    """A class that inherits from list."""
    pass

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(list(self)))
