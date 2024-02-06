#!/usr/bin/python3
"""Provides a function to convert a JSON string back into a Python object."""
import json

def from_json_string(my_str):
    """Converts a JSON-formatted string into its corresponding Python object.

    Args:
        my_str: A string in JSON format.

    Returns:
        The Python object derived from the JSON string.
    """
    return json.loads(my_str)
