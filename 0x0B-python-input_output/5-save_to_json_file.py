#!/usr/bin/python3
"""Function writes an object to a text file, using JSON"""
from json import dump


def save_to_json_file(my_obj, filename):
    """ this convert python obj into json string and write to file"""
    with open(filename, "w", encoding="utf-8") as f:
        dump(my_obj, f)
