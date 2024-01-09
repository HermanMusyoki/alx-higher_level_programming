#!/usr/bin/python3
"""Defines a function to read files"""


def read_file(filename=""):
    """outputs the contents of a UTF8 text file to standard output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
