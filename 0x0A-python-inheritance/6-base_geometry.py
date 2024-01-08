#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Base geometry representation"""

    def area(self):
        """Area not computed"""
        raise Exception("area() is not implemented")
