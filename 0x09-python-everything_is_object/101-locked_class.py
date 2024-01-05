#!/usr/bin/python3
"""Defines a Locked class"""


class LockedClass:
    """
    prohibits the user from creating a new class or objects attributes,
    only first_name attribute can be created
    """

    __slots__ = ["first_name"]
