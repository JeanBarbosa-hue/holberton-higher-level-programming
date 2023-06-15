#!/usr/bin/python3

"""Contains class called square."""


class Square:
    """Class called square for printing hashtag."""

    def __init__(self, size=0):
        """Constructor method."""
        self.size = size

    def size(self):
        """Property getter method."""
        return self.__size

    def size(self, value):
        """Property setter method."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method to calculate square area."""
        return self.__size ** 2

    def my_print(self):
        """Method to print hashtag."""
        if self.size == 0:
            print("")
        else:
            for row in range(self.size):
                print("#" * self.size)
