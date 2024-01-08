#!/usr/bin/python3
"""Module to import_from"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Raises an exception, area not implemented"""
        raise Exception("area() is not implemented")
