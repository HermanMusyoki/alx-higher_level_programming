#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square representation"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): attribute for square side length.
            position (int, int): New square position attribute
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """method for setter and getter square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """method for getter and setter of square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return computed square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print a square using # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
