#!/usr/bin/python3
"""Module for Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.validate("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.validate("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle."""
        self.validate("x", value, True)
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle."""
        self.validate("y", value, True)
        self.__y = value

    @staticmethod
    def validate(attribute, value, non_negative):
        """Validate an attribute with its value."""
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if non_negative and value < 0:
            raise ValueError(f"{attribute} must be >= 0")
        if not non_negative and value <= 0:
            raise ValueError(f"{attribute} must be > 0")
