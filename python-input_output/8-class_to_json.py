#!/usr/bin/python3

"""returns the dictionary description with a simple
data structure for a JSON serialization of an object.
"""


def class_to_json(obj):
    """Method that retuns the dictionary description of an object."""

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
