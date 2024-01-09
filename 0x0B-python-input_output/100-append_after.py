#!/usr/bin/python3
"""Defines a function for inserting a text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing specific string

    Args:
        filename (str): The name of the file.
        search_string (str): search string from the file
        new_string (str): the string containing text to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
