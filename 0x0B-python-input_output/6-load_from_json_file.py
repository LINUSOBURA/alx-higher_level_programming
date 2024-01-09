#!/usr/bin/python3
"""Create abject from Json file"""
import json


def load_from_json_file(filename):
    """Function creates an object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
