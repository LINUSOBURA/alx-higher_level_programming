#!/usr/bin/python3
"""Module converts class to json"""


def class_to_json(obj):
    """converts a class to a serializable dictionary"""
    serializable_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
    return serializable_dict
