#!/usr/bin/python3
"""
Finds a list of attributes and methods of the object.
"""


def lookup(obj):
    """Returns that list of attributes & methods.

    Args:
        - obj: object to look into
    """

    return dir(obj)
