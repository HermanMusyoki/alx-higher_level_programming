#!/usr/bin/python3
"""Defines class MyList derived from list"""


class MyList(list):
    """prints the list in ascending sort using built-in mechanism"""

    def print_sorted(self):
        """Return sorted list"""
        print(sorted(self))
