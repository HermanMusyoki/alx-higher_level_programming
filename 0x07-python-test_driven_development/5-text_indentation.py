#!/usr/bin/python3
"""Defines a function for text indentation"""


def text_indentation(text):
    """Print text with 2 new lines after each . , ? and :

    Args:
        text (string): The text to be printed
    Raises:
        TypeError: if the line text is not a string value
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
