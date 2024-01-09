#!/usr/bin/python3
"""Defines a function to write a string"""


def write_file(filename="", text=""):
    """Write a string to text file in UTF8

    Args:
        filename (str): the file name to write to
        text (str): The textcontents to write to the file.
    Returns:
        The number of characters to write in the text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
