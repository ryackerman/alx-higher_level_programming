#!/usr/bin/python3
"""
Defines the Base class
"""


class Base:
    """
    Base class for managing id attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init a Base instance
        Args:
            id (int): Optional. The id value for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
