#!/usr/bin/python3
"""Module to save object to file"""
import json


def save_to_json_file(my_obj, filename):
    """Function saves object to json file"""
    with open(filename, "a") as f:
        return json.dump(my_obj, f)
