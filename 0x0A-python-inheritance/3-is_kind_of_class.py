#!/usr/bin/python3
"""
Function to check if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if instance else False"""
    return True if isinstance(obj, a_class) else False
