#!/usr/bin/python3
"""a function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """
     Load a Python object from a JSON-formatted file.

    Parameters:
    - filename: The name or path of the file to be read.

    Returns:
    object: The Python object loaded from the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
