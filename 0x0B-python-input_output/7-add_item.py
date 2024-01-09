#!/usr/bin/python3
"""Scrript to Load add and save in file"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

arguments = sys.argv
filename = "add_item.json"

try:
    arg_list = load_from_json_file(filename)
except FileNotFoundError:
    arg_list = []

arg_list.extend(arguments[1:])

save_to_json_file(arg_list, filename)

if __name__ == "__main__":
    pass
