#!/usr/bin/python3

"""writes a string to a text file and
returns the number of characters written."""


def write_file(filename="", text=""):
    """write string to text."""
    with open(filename, 'w') as file:
        return file.write(text)
