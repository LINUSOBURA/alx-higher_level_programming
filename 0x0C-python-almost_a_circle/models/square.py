#!/usr/bin/python3
"""Square Module that inherits from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherit from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """Function  to update attributes depending on arguments"""
        attributes = ["id", "size", "x", "y"]

        for i, attr_value in enumerate(args):
            setattr(self, attributes[i], attr_value)

        if not args:
            for attr in attributes:
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """Function to convert rectangle instance to dict representatiom"""
        dict = {
            "id": self.id,
            "x": self.x,
            "size": self.height,
            "size": self.width,
            "y": self.y,
        }
        return dict

    def to_csv(self):
        """Return a CSV representation of the Square instance"""
        return [self.id, self.size, self.x, self.y]

    @classmethod
    def create_from_csv(cls, csv_row):
        """Create a Square instance from a CSV row"""
        return cls(*map(int, csv_row))
