#!/usr/bin/python3
"""Module to convert from Json string to object"""
import json


def from_json_string(my_str):
    """Function that returns an object represented by a JSON string"""
    return json.loads(my_str)
