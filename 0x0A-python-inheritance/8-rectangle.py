#!/usr/bin/python3
"""Defines a class Rectangle inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle representation from BaseGeometry."""

    def __init__(self, width, height):
        """New Rectangle initialization

        Args:
            width (int): new Rectangle width
            height (int): new Rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
