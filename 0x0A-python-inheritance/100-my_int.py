#!/usr/bin/python3
"""Defines a class MyInt a subclass of int"""


class MyInt(int):
    """interchange int operators == and !="""

    def __eq__(self, value):
        """change == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """change != operator with == behavior"""
        return self.real == value
