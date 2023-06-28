#!/usr/bin/python3

"""defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Init of a square.

        Args:
            size(int): size of a new square"""
        self.size = size
        self.position = position

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
        else:
            self.__size = value

    def area(self):
        """returns the current square area.

        Returns:
            int: The area of the square."""
        return (self.__size * self.__size)

    @property
    def position(self):
        """retrieves position of a square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter

        Args:
            value(tuple): position of a new square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square using the character '#'"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
