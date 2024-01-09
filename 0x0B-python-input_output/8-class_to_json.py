#!/usr/bin/python3
"""Defines a function returns a JSON from a class"""


def class_to_json(obj):
    """Return a simple data structure represented by a dictionary"""
    return obj.__dict__
