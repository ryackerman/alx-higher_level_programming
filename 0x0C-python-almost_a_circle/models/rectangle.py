#!/usr/bin/python3
"""
Defines the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init a Rectangle instance
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): Optional. The x-coordinate of the rectangle's position.
            y (int): Optional. The y-coordinate of the rectangle's position.
            id (int): Optional. The id value for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Setter for x attribute"""
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Setter for y attribute"""
        self.__y = value
