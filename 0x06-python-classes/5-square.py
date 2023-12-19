#!/usr/bin/python3
"""Square class for representing a square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0):
        """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """getter to retrieve the private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter to set the attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
