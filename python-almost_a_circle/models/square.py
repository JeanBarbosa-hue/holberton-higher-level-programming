#!/usr/bin/python3

"""module with class called square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class called square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size

        Args:
            value (int): value to set size to
        """
        self.width = value
        self.height = value

    def __str__(self):
        """string method"""
        id_str = str(self.id)
        x_str = str(self.x)
        y_str = str(self.y)
        size_str = str(self.size)
        square_str = "[Square] (" + str(self.id) + ") " + str(self.x) + \
            "/" + str(self.y) + " - " + str(self.width)
        return square_str

    def update(self, *args, **kwargs):
        """update method"""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary method"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
