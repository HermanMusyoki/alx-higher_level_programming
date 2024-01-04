#!/usr/bin/python3
"""Define Rectangle class."""


class Rectangle:
    """Rectangle represantion"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): new rectangle width
            height (int): new rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))