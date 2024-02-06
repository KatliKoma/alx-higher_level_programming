#!/usr/bin/python3
"""
Provides a function that converts an object's attributes
into a dictionary for easy JSON serialization,
supporting simple data structures like lists, dictionaries,
strings, integers, and booleans.
"""

def class_to_json(obj):
    """Creates a dict description of obj.

    Args:
        - obj: object to serialize

    Returns: dictionnary description of obj
    """

    return obj.__dict__
