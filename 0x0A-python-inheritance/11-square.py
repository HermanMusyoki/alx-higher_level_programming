#!/usr/bin/python3
"""Defines a Square inherited from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square represenation"""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): new square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
