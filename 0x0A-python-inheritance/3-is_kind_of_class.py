#!/usr/bin/python3
"""Defines a class and inherited object instance"""


def is_kind_of_class(obj, a_class):
    """determines whether object is class instance or inherited instance..

    Args:
        obj (any): The object to determine
        a_class (type): The class to compare the type of object to.
    Returns:
        True - Object is an instance or inherited instance of a_class
        False - otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
