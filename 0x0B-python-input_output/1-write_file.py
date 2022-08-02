#!/usr/bin/python3
"""Contains function definition that writes a string to a text file
    and returns the number of characters"""


def write_file(filename="", text=""):
    """Function definition"""

    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            text = f.write(type(str("")))
            print(len(text), end="")
