#!/usr/bin/python3
"""Function that compares if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Returns True if exactly instance else false"""
    if type(obj) is a_class:
        return True
    else:
        False
