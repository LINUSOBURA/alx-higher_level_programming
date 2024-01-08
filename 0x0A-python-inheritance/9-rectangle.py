#!/usr/bin/python3
"""Module with class Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Initialized with width and height both private"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    @property
    def width(self):
        """Getter function to get width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function to set width value"""
        self.__width = value

    @property
    def height(self):
        """Getter function to get height value"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter function to set height value"""
        self.__height = value

    def area(self):
        """Method that returns area of a rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
