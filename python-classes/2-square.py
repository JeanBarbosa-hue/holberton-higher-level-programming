#!/usr/bin/python3

"""This method contains a class called square."""


class Square:

    """A class with a private instance."""

    def __init__(self, size=0):
        """Size with new instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
