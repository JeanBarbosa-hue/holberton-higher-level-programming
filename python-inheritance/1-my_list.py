#!/usr/bin/python3

"""Class called MyList that inherits list."""


class MyList(list):
    """Print list in ascended order."""

    def print_sorted(self):
        ascend_list = sorted(self)
        print(ascend_list)
