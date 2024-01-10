#!/usr/bin/python3
"""Module to add 2 integers"""


def add_integer(a, b=98):
    """Function adds 2 integers and returnsan int"""

    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    if (isinstance(x, float) for x in (a, b)):
        a = int(a)
        b = int(b)

    return a + b
