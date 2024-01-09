#!/usr/bin/python3
"""Defines a function to append a string"""


def append_write(filename="", text=""):
    """Appends a string to the end of the text file in UTF8

    Args:
        filename (str): The name of the file to append characters
        text (str): The string to add to the file.
    Returns:
        The number of characters to append to the text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
