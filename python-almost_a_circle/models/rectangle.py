#!/usr/bin/python3

"""Module with class called rectangle."""

from models.base import Base


class Rectangle(Base):
    """class rectangle that inherits base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def width(self):
        return (self.__width)

    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be a integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    def height(self):
        return (self.__height)

    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be a integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    def x(self):
        return (self.__x)

    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be a int")
        if value <= 0:
            raise ValueError("x must be > 0")

    def y(self):
        return (self.__y)

    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be a int")
        if value <= 0:
            raise ValueError("y must be > 0")
