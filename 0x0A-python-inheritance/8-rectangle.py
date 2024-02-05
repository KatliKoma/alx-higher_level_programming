#!/usr/bin/python3

def __init__(self, width, height):
    """Initializes an instance of Rectangle.

    Args:
        - width: the width of the rectangle
        - height: the height of the rectangle
    """
    # Calling integer_validator method from the base class for width and height.
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    # Setting private instance attributes __width and __height.
    self.__width = width
    self.__height = height
