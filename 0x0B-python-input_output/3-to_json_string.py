#!/usr/bin/python3
"""Provides a function to convert objects to their JSON string representation."""
import json

def to_json_string(my_obj):
    """Converts and returns an object's JSON string representation.

    Parameters:
        my_obj: The object to be converted into JSON format.
    Returns:
        str: A JSON-formatted string representation of the object.
    """
    return json.dumps(my_obj)
