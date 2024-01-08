#!/usr/bin/python3
"""Defines a class Rectangle inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle representation from BaseGeometry."""

    def __init__(self, width, height):
        """Instance of  a new Rectangle.

        Args:
            width (int): new Rectangle width
            height (int): new Rectangle height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() that represents the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
