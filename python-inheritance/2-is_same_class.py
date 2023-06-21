#!/usr/bin/python3

"""Funcion that returns True if object is exactly instance of specified class."""


def is_same_class(obj, a_class):
    """Return True if object is instance else false."""
    if type(obj) is a_class:
        if isinstance(obj, a_class):
            return True
    else:
        return False
