#!/usr/bin/ptyhon3
"""
This program validate the kind of an obj
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is am instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise; otherwise False.
    """
    return isinstance(obj, a_class)
