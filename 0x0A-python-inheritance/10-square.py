#!/usr/bin/python3
"""Module with square """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Init method to initialize a square and inherit from rectangle"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
