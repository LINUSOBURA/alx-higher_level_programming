#!/usr/bin/python3
"""Module for writing to a file"""


def write_file(filename="", text=""):
    """Funtion writes to a file, and return number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
