#!/usr/bin/python3
"""Function writes an object to a text file, using JSON"""
import json as js


def save_to_json_file(my_obj, filename):
    """ this convert python obj into json string and write to file"""
    with open(filename, "w",) as f:
        js.dumps(my_obj, f)
