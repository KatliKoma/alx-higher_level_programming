#!/usr/bin/python3
"""
Generates a Python object based on the content of a JSON file.
"""

import json

def load_from_json_file(filename):
    """Generates and returns a Python object from a specified JSON file.
    Parameters:
        - filename: The name of the file containing JSON data.
    Returns:
        The Python object created from the JSON file's data.
    """

    with open(filename, 'r') as f:
        return json.load(f)
