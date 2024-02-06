#!/usr/bin/python3
"""
Provides a function that converts an object's attributes
into a dictionary for easy JSON serialization,
supporting simple data structures like lists, dictionaries,
strings, integers, and booleans.
"""

def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
