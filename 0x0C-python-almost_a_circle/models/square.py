#!/usr/bin/python3
"""Defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Init a Square instance
        Args:
            size (int): The size of the square.
            x (int): Optional. The x-coordinate of the square's position.
            y (int): Optional. The y-coordinate of the square's position.
            id (int): Optional. The id value for the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the square"""
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
        }
