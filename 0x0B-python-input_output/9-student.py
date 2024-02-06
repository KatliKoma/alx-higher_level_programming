#!/usr/bin/python3
"""Module 9-student.
Introduces the Student class for creating student objects.
"""

class Student:
    """Defines a student with attributes and methods.
    Attributes:
        - first_name: First name of the student.
        - last_name: Last name of the student.
        - age: Age of the student.
    Methods:
        - to_json: Returns a dictionary representation of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Constructs a new Student object with the given attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts the student object to a dictionary format.
        Returns: A dictionary containing the student's attributes.
        """

        return self.__dict__
