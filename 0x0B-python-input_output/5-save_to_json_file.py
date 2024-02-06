#!/usr/bin/python3
"""Provides a function to save an object to a file in JSON format."""
import json

def save_to_json_file(my_obj, filename):
    """Saves a given object as a JSON string in a specified file.

    Args:
        my_obj: The object to be saved in JSON format.
        filename: The name of the file where the JSON representation will be written.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
