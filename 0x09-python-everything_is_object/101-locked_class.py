#!/usr/bin/python3
"""A locked class with no attributes"""


class LockedClass:
    """Locked class prevents dynamic creation of instance attributes"""

    __slots__ = ("first_name",)

    def __init__(self):
        self.first_name = None
