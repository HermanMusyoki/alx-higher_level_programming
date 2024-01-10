#!/usr/bin/python3
"""Defines a function to find the max integer in a list
"""


def max_integer(list=[]):
    """Return the max integer in a list of integers
        for an empty list return NONE
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
