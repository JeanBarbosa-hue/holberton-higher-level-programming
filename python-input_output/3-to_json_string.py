#!/usr/bin/python3

""" contains a function thatreturn the
JSON representation of an object."""

import json


def to_json_string(my_obj):
    """Function that returns a JSON."""
    json_str = json.dumps(my_obj)
    return json_str
