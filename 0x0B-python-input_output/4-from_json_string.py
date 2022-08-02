#!/usr/bin/python3
""" defines json_to_python function"""
import json as js


def from_json_string(my_str):
    """ changes json to python obj"""
    return (js.loads(my_str))
