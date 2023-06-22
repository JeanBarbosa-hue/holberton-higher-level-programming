#!/usr/bin/python3

"""Reads file and prints it stdout."""


def read_file(filename=""):
    """Method to read file."""
    with open(filename, 'r') as file:
        for i in file:
            print(i, end="")
