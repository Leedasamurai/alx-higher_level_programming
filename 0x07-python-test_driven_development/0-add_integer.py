#!/usr/bin/python3
def add_integer(a, b=98):
    """

    adds 2 integers.

    Args:
    - a: int or float
    - b: int or float (default = 98)

    Return:
    -Int: the addition of a and b

    """

    if not isinstance(a , (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int,float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
