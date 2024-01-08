#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Base geometry representation"""

    def area(self):
        """Area not computed"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check a value as an integer.

        Args:
            name (str): the name of value 
            value (int): The parameter to be checked.
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is greater or equals zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
