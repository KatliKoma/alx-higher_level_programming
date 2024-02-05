#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a Square."""
    
    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The side length of the square.
        """
        # Validate the 'size' parameter as an integer and store it as the width and height.
        self.integer_validator("size", size)
        super().__init__(size, size)
    
    def area(self):
        """Calculate and return the area of the square."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Square object."""
        return "[Square] {}/{}".format(self.__width, self.__height)
