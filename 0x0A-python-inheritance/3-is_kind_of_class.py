#!/usr/bin/python3
"""
This module, named `is_kind_of_class`, determines whether an object belongs to a specific class or inherits from any of its subclasses.

For example, if we have the following class hierarchy:
"""


def is_kind_of_class(obj, a_class):
    """if obj is an instance of a_class or a class
    inherited from a_class.

    Args:
        - obj: object to be checked
        - a_class: class to evaluate

    Returns: True or False
    """

    return isinstance(obj, a_class)
