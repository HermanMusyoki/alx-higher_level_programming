#!/usr/bin/python3
"""Defines an inherited to determine object instance"""


def inherits_from(obj, a_class):
    """detrmine whether object is an inherited instance of a class.

    Args:
        obj (any): The object to determine
        a_class (type): The class to compare the type of obj to.
    Returns:
        True - Object is an inherited instance of a_class
        False - otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
