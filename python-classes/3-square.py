#!/usr/bin/python3

"""Contains a class called square."""


class Square:

    """Class which has private instance"""

    def __init__(self, size=0):
        """Size with new instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method with square area."""
        return self.__size ** 2
