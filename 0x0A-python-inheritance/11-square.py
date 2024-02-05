#!/usr/bin/python3
"""This script defines a Square class that is a subclass of Rectangle."""
from importlib import import_module

# Import the Rectangle class from the '9-rectangle' module.
Rectangle = import_module('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a geometric square."""

    def __init__(self, size):
        """Creates a new square object.

        Args:
            size (int): The side length of the square.
        """
        # Validate the 'size' parameter as an integer.
        self.integer_validator("size", size)
        # Initialize the square by calling the parent class constructor with 'size' for both width and height.
        super().__init__(size, size)
        # Set the private instance attribute '__size' to the provided 'size'.
