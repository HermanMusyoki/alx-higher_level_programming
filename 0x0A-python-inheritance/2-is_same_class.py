#!/usr/bin/python3
"""Defines a function to check object instance"""


def is_same_class(obj, a_class):
    """Determines if the object is an instance of class

    Args:
        obj (any): The object to determine.
        a_class (type): The class to compare the type of object to.
    Returns:
        True- object is exactly class instance
        False - otherwise
    """
    if type(obj) == a_class:
        return True
    return False
