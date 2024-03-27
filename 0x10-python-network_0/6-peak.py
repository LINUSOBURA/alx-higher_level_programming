#!/usr/bin/python3
"""Finding the peak in a List"""


def find_peak(list_of_integers):
    """Function to find peak"""
    max = 0
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    for i in list_of_integers:
        if i > max:
            max = i
    return max
