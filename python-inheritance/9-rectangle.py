#!/usr/bin/python3

"""Class called BaseGeometry."""


class BaseGeometry:
    """Public instance that raises exception."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")


"""Class called rectangle that inherits from basegeometry."""


class Rectangle(BaseGeometry):
    """child class called rectangle."""

    def __init__(self, width, height):
        """construtor method."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate height and width method."""
        return self.__width * self.__height

    def __str__(self):
        """Method for rectangle description."""
        return ("[Rectangle]{}/{}".format(self.__width, self.__height))
