#!/usr/bin/python3
"""A func of json str"""
import json


def from_json_string(my_str):
    """return the Python object representation of a JSON string."""
    return json.loads(my_str)
