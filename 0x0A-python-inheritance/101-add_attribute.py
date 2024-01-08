#!/usr/bin/python3
"""Module to add non existing attribute"""


def add_attribute(obj, attr, value):
    """Adds an attribute if possible"""
    if hasattr(obj, "__dict__") or (
        hasattr(type(obj), "__slots__") and attr in type(obj).__slots__
    ):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
