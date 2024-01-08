#!/usr/bin/python3
"""Module to import_from"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Raises an exception, area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates if valu is int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
