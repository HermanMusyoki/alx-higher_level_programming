#!/usr/bin/python3
"""Defines function that sum 2 integers"""


def add_integer(a, b=98):
    """Return the sum of integers a and b.

    typecaste float to integer before addition

    Raises:
        TypeError: If either of a or b is not integer or flaot
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
