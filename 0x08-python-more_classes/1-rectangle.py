#!/usr/bin/python3

""" A simple rectangle class"""


class Rectangle():
    """
    A class rectangle for creating a rectagle
    """
    def __init__(self, width=0, height=0):
        """
        Creates a new instance of rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter to retrieve private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to modify private attribute height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Getter to retrieve private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to modify private attribute width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
