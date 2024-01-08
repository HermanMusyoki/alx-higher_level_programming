#!/usr/bin/python3
"""Defines a function that adds objects attributes"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object

    Args:
        obj (any): The object for attributed to be added
        att (str): The attribute name to be added to object
        value (any): The attribute value to add
    Raises:
        TypeError: If not possible to add an attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
