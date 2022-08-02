#!/usr/bin/python3

"""
Contains definition of a function that reads a text file
"""


def read_file(filename=""):
    """Definition of a function that reads a text file
        Args:
            filename="" which defines the filename.
    """
    with open('UTF8', encoding='utf-8') as filename:
        fileread = filename.read()
        print(fileread)
