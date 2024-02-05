#!/usr/bin/python3
"""Module 7-base_geometry.
Defines a class called BaseGeometry with public instance methods.
"""


class BaseGeometry:
    """A class with public instance methods 'area' and 'integer_validator'."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates 'value' to ensure it's an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
