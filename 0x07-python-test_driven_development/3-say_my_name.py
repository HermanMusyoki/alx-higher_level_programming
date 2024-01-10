#!/usr/bin/python3
"""Defines a function that prints name"""


def say_my_name(first_name, last_name=""):
    """Output a name.

    Args:
        first_name (str): parameter for first name to be printed
        last_name (str): parameter for last name to be printed
    Raises:
        TypeError: If first name or last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
