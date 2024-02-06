#!/usr/bin/python3
"""
This module, named `is_kind_of_class`, determines whether an object belongs to a specific class or inherits from any of its subclasses.

For example, if we have the following class hierarchy:
"""

def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    or a class that the class in question inherits from
    """
    return (isinstance(obj, a_class))
