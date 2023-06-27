#!/usr/bin/python3

"""defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Init of a square.

        Args:
            size(int): size of a new square"""
        self.__size = size

    @property
    def size(self):
        """retrieves size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area."""
        return (self.__size * self.__size)

