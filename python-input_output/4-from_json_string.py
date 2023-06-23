#!/usr/bin/python3

"""function that return an object represented by a JSON string."""
import json


def from_json_string(my_str):
    """Function that returns an objec JSON ."""
    return json.loads(my_str)
