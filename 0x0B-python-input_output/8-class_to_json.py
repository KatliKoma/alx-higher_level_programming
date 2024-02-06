#!/usr/bin/python3
"""Module 8-class_to_json.
Provides a function that converts an object's attributes
into a dictionary for easy JSON serialization,
supporting simple data structures like lists, dictionaries,
strings, integers, and booleans.
"""

def class_to_json(obj):
    """Generates a dictionary representation of an object for JSON serialization.

    Parameters:
        - obj: The object to be serialized.

    Returns:
        A dictionary representation of the object's attributes.
    """

    return obj.__dict__
