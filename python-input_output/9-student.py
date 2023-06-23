#!/usr/bin/python3

"""retrieves a dictionary representation of a Student instance."""


class Student:
    """class called student"""

    def __init__(self, first_name, last_name, age):
        """set first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary"""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
