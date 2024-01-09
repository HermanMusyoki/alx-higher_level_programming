#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """new student representation"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Use dictionary to  represent the Student object

        only attributes in the list should be represented not strings

        Args:
            attrs (list): attributes to be represented in the object
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
