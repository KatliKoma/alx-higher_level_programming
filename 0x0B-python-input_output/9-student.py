#!/usr/bin/python3
"""Module for defining the Student class."""

class Student:
    """A class for creating student objects."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.
        
        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the instance.
        
        Returns:
            A dictionary containing all the key/value pairs of the instance's attributes.
        """
        return self.__dict__.copy()
