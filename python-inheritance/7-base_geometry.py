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
                raise TypeError("<name> must be an integer")
            if value <= 0:
                raise ValueError("<name> must be greater than 0")
