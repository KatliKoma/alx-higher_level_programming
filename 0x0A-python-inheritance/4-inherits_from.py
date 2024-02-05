#!/usr/bin/python3
"""Module 4-inherits_from.
Checks whether an object is an instance of a class that inherits
either directly or indirectly from a specified class.
"""


def inherits_from(obj, a_class):
    """Determines if 'obj' is an instance of a class that
    has inherited (either directly or indirectly) from 'a_class'.

    Args:
        - obj: The object to be examined.
        - a_class: The class being assessed.

    Returns: True if it is an instance, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
