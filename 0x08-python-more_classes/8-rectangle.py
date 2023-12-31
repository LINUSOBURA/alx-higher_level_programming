#!/usr/bin/python3

""" A simple rectangle class"""


class Rectangle():
    """Public class attributes"""
    number_of_instances = 0
    print_symbol = '#'

    """
    A class rectangle for creating a rectagle
    """
    def __init__(self, width=0, height=0):
        """
        Creates a new instance of rectangle
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Gets the area of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height * self.__width

    def perimeter(self):
        """Gets the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += str(Rectangle.print_symbol) * self.__width
                + "\n"
            return rectangle_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
