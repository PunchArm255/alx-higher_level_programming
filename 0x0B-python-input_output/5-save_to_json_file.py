#!/usr/bin/python3
"""
This is '5-save_to_json_file' module.
Functions and Classes:
    save_to_json_file(my_obj, filename)
"""


def save_to_json_file(my_obj, filename):
    """write obj to txt in JSON"""
    from json import dump
    with open(filename, "w", encoding="UTF-8") as f:
        dump(my_obj, f)
