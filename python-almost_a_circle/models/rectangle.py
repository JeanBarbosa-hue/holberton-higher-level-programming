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
