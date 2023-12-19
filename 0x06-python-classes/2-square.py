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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
