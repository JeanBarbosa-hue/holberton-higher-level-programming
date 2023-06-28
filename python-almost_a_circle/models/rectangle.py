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

    def width(self):
        """width getter"""
        return (self.__width)

    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be a integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def height(self):
        """height getter"""
        return (self.__height)

    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be a integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def x(self):
        """x getter"""
        return (self.__x)

    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be a int")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    def y(self):
        """y getter"""
        return (self.__y)

    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be a int")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value
