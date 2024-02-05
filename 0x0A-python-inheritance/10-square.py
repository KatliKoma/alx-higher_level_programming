#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new square instance.

        Args:
            size (int): The size of the new square.
        """
        # Validate the 'size' parameter as an integer.
        self.integer_validator("size", size)
        # Initialize the square by calling the parent class constructor with 'size' for both width and height.
        super().__init__(size, size)
        # Set the private instance attribute '__size' to the provided 'size'.
