#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """
    Return a Python data structure represented by a JSON string.

    Parameters:
    - my_str (str): The JSON string to be converted.

    Returns:
    object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
