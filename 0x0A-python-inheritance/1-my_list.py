#!/usr/bin/python3
"""Class my list inherit list"""


class MyList(list):
    def print_sorted(self):
        """Prints sorted list"""
        sorted_l = sorted(self)
        print(sorted_l)
