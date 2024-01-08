#!/usr/bin/python3
"""Class my list inherit list"""


class MyList(list):
    """MyList class has one method print_sorted"""

    def print_sorted(self):
        """Prints sorted list"""
        sorted_l = sorted(self)
        print(sorted_l)
