#!/usr/bin/python3

"""Class called MyList that inherits list."""


class MyList(list):
    """Class to print list in ascended order."""

    def print_sorted(self):
        """Print list in ascended order."""
        ascend_list = sorted(self)
        print(ascend_list)
