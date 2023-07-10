#!/usr/bin/python3
"""defines an object attribute lookup function."""


def lookup(obj):
    """a function that returns the list of available attributes and methods of an object.

    Args:
        obj: object to inspect.

    Returns:
        list: a list object.
    """
    return dir(obj)
