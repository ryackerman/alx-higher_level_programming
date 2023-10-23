#!/usr/bin/python3

def print_square(size):
    """Prints a square of size length using the character '#'.

    Args:
        size (int): The size length of the square.
        
    Raises:
        TypeError: If size is not an integer or a float.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
