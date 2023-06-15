#!/usr/bin/python3

"""Contains class called square."""


class Square:
    """Class containing a constructor, property, property setter, instantiation and square area.
    """

    def __init__(self, size=0):
        """This is a constructor method."""
        self.size = size

    @property
    def size(self):
        """This is a property method."""
        return self.__size

    @size.setter
    def size(self, value):
        """This is property setter method."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate square area method."""
        return self.__size ** 2
