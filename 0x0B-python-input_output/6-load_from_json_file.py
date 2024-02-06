#!/usr/bin/python3
"""Implements a function for loading objects from JSON files."""
import json

def load_from_json_file(filename):
    """Generates a Python object from the contents of a JSON file.

    Args:
        filename: The path to the JSON file to be read.

    Returns:
        The Python object represented by the JSON data in the file.
    """
    with open(filename) as f:
        return json.load(f)
