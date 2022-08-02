#!/usr/bin/python3
"""Function appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string and returns the number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
