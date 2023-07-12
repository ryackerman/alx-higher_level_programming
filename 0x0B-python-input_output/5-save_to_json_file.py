#!/usr/bin/python3
"""A func that writes an obj to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Object to a text file using json representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
