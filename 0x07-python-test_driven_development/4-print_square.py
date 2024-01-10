#!/usr/bin/python3
"""Module to print square"""


def print_square(size):
    """Function prints # for the size of square"""
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    if not (isinstance(size, float)) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
