#!/usr/bin/python3
"""Provides a function to add content to an existing file."""

def append_write(filename="", text=""):
    """Adds a specified string to the end of a UTF-8 encoded text file.

    Parameters:
        filename (str): The file to which the string will be added.
        text (str): The content to be added to the file.
    Returns:
        int: The count of characters that were added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
