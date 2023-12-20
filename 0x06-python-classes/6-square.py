#!/usr/bin/python3
"""Square class for representing a square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
            or not all(
                isinstance(i, int) or isinstance(i, str) and i.isdigit() for i in value
            )
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
