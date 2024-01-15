#!/usr/bin/python3
"""Rectangle module, inherits from Base"""
from .base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the rectangle.
        - y (int): The y-coordinate of the rectangle.
        - id (int): The identifier for the rectangle.
        """
        id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function to get area"""
        result = self.__width * self.__height
        return result

    def display(self):
        """function to display the rectangle using #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
            - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Function updates attributes depending on arguments"""
        attributes = ["id", "width", "height", "x", "y"]

        for i, attr_value in enumerate(args):
            setattr(self, attributes[i], attr_value)

        if not args:
            for attr in attributes:
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """Function to convert rectangle instance to dict representatiom"""
        dict = {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
        return dict
