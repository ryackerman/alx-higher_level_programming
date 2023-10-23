#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds 2 integers
    Args:
        a (int or a float): first number
        b (int or a float): second number, its default value=98
    Returns:
        int: sum of a and b
    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
