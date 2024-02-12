#!/usr/bin/python3
"""Module for Base class."""

class Base:
    """Base class for future classes."""
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """Class constructor.
        
        Args:
            id (int): The id of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
