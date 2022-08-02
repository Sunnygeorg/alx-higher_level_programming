#!/usr/bin/python3

"""
Contains definition of a function that reads a text file
"""


def read_file(filename=""):
    """Definition of a function that reads a text file"""
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
            print(text, end="")
