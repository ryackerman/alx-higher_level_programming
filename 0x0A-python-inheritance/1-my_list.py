#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """a class that inherits from list"""
    def __init__(self):
        """init the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted in ascending order."""
        print(sorted(self))
