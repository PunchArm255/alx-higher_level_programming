#!/usr/bin/python3
"""
This is '6-load_from_json_file' module.
Functions and Classes:
    load_from_json_file(filename)
"""


def load_from_json_file(filename):
    """create obj from JSON"""
    from json import load
    with open(filename, "r", encoding="UTF-8") as f:
        obj = load(f)

    return obj
