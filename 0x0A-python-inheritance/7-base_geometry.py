#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """A base geometry-related class BaseGeometry."""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If value <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
