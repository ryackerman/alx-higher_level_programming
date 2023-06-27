#!/usr/bin/python3

"""defines a square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Init of a square.

        Args:
            size(int): size of a new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area."""
        return (self.__size * self.__size)
