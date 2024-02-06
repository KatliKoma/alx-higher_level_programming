#!/usr/bin/python3
"""Module for generating a Python object from a JSON file."""
import json

def load_from_json_file(filename):
    """Generates a Python object based on a JSON file's content.

    Parameters:
        filename: The name of the file containing JSON data.

    Raises:
        Exception: If there's an issue decoding the JSON data.

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
