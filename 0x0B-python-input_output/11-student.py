#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """student representation"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): student age attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """find Student dict representation

        only represent attributes contained in the list of strings

        Args:
            attrs (list): attributes representation
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """change all attributes of the Student using dictionary

        Args:
            json (dict): the dictionary used to replace the attributes
        """
        for k, v in json.items():
            setattr(self, k, v)
