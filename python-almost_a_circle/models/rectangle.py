#!/usr/bin/python3

"""Module with class called rectangle."""

from models.base import Base


class Rectangle(Base):
    """class rectangle that inherits base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method"""
        return (self.__width)

    def width(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """getter method"""
        return (self.__height)

    def height(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """getter method"""
        return (self.__x)

    def x(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """getter method"""
        return (self.__y)

    def y(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
