#!/usr/bin/python3
"""Finding the peak in a List"""


def find_peak(list_of_integers):
    """Function to find peak"""
    if not list_of_integers:
        return None
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        midium = (left + right) // 2

        if list_of_integers[midium] > list_of_integers[
                midium -
                1] and list_of_integers[midium] > list_of_integers[midium + 1]:
            return list_of_integers[midium]
        elif list_of_integers[midium] < list_of_integers[midium + 1]:
            left = midium + 1
        else:
            right = midium - 1
    return list_of_integers[left]
