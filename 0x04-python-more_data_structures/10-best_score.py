#!/usr/bin/python3


def best_score(a_dictionary):
    max_value = 0
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > max_value:
                max_value = a_dictionary[key]
                maximum = key
        return maximum
    else:
        return None
