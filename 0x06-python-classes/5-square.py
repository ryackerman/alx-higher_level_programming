#!/usr/bin/python3

"""defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Init of a square.

        Args:
            size(int): size of a new square"""
        self.size = size

    @property
    def size(self):
        """retrieves size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter

        Args:
            value(int): size of a new square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area.

        Returns:
            int: The area of the square."""
        return (self.__size * self.__size)
    
    def my_print(self):
        """prints the square using the character '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
