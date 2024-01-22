#!/usr/bin/python3
def raise_exception():
    raise TypeError("Exception raised")

# Example usage
try:
    raise_exception()
except TypeError as te:
    print(te)
