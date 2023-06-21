#!/usr/bin/python3

"""List all attributes and methods."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    attributes = dir(obj)
    return (attributes)
