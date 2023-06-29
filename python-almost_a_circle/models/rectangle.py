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
        """property"""
        return (self.__width)

    def width(self, value):
        """setter method"""
        self.__width = value

    def height(self):
        """property"""
        return (self.__height)

    def height(self, value):
        """setter method"""
        self.__height = value

    def x(self):
        """property"""
        return (self.__x)

    def x(self, value):
        """setter method"""
        self.__x = value

    def y(self):
        """property"""
        return (self.__y)

    def y(self, value):
        """setter method"""
        self.__y = value
