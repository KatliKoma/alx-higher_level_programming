#!/usr/bin/python3

def area(self):
    """This method is currently unimplemented."""
    raise Exception("area() has not been implemented yet")

def integer_validator(self, name, value):
    """Validates a parameter as an integer.

    Args:
        name (str): The name of the parameter.
        value (int): The parameter to validate.
    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
    """
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
