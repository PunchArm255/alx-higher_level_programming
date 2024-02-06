#!/usr/bin/python3
"""
This is '3-to_json_string' module.
Functions and Classes:
    to_json_string(my_obj)
"""


def to_json_string(my_obj):
    """ret JSON rep of obj"""
    import json
    return json.dumps(my_obj)
