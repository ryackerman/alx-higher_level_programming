#!/usr/bin/python3
"""A subclass representing a Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes a square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
