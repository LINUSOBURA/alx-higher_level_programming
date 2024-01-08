#!/usr/bin/python3
"""Module with square """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Init method to initialize a square and inherit from rectangle"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
