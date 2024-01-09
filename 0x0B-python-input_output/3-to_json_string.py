#!/usr/bin/python3
""" To JSON string """
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string) """
    text = json.dumps(my_obj)
    return text
