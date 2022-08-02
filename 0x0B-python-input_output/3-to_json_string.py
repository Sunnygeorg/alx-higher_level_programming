#!/usr/bin/python3
"""Function returns JSON representation of an object"""

def to_json_string(my_obj):
    """ Returns JSON reprenstation of a string"""
    import json
    obj = json.dumps(type(str(my_obj)))
    return(obj)
