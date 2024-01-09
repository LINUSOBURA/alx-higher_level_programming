#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """Function reads a file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
