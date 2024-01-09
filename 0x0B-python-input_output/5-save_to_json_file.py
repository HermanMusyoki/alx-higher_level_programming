#!/usr/bin/python3
"""Defines a function that converts an object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Use JSON representation to write an object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
