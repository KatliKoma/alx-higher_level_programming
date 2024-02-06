#!/usr/bin/python3
"""JSON-to-object function."""
import json


def from_json_string(my_str):
    """Convert a JSON string into its equivalent Python object representation."""
    return json.loads(my_str)
