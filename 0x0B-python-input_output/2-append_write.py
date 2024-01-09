#!/usr/bin/python3
"""Module that appends string to a file"""


def append_write(filename="", text=""):
    """Function appends texts to a flile"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
