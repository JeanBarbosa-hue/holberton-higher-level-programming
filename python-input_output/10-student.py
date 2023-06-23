#!/usr/bin/python3

"""class called Student"""


class Student:
    """class called student"""

    def __init__(self, first_name, last_name, age):
        """method that set first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary"""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
