#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """New student representation"""

    def __init__(self, first_name, last_name, age):
        """Initialize an instance of a new Student.

        Args:
            first_name (str): Student first name
            last_name (str): Student last name
            age (int): The parameter for age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Represent the Student using a dictionary"""
        return self.__dict__
