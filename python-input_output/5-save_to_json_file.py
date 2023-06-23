#!/usr/bin/python3

"""writes an object to
a text file using a JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Mehod that writes an object using a JSON representation."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
