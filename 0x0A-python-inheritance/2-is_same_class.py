#!/usr/bin/python3
"""
Finds an object is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """determines if obj is an instance of a_class.

    Args:
        - obj: object to look at
        - a_class: class to verify the instance of

    Returns: True if obj is an instance of a_class.
    """

    return True if type(obj) is a_class else False
