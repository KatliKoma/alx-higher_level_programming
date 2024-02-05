#!/usr/bin/python3
"""Module 6-base_geometry.
Defines a class with a public instance method.
"""


class BaseGeometry:
    """A class with a public instance method 'area'."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'.
        """
        raise Exception('area() is not implemented')
