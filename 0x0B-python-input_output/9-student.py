#!/usr/bin/python3
""" Module designed to generate a dictionary representation 
    using simple data structures, facilitating the JSON serialization of an object.
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
