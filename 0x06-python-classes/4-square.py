#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square representation."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): attribute for the side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """method for getter and setter of new square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return computed square area"""
        return (self.__size * self.__size)
