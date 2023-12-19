#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square representation"""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): attribute for the side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """method for setter and getter of size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the computed square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square using # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
