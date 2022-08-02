#!/usr/bin/python3
"""Function returns JSON representation of an object"""
import json


def to_json_string(my_obj):
    """ Returns JSON reprenstation of a string"""
    obj = json.dumps(my_obj)
    return(obj)
