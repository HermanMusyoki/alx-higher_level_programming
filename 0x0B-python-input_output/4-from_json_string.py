#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function that converts JSON to object"""
import json


def from_json_string(my_str):
    """Return an object that is represented by a JSON string."""
    return json.loads(my_str)
