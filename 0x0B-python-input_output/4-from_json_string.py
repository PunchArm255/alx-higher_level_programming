#!/usr/bin/python3
"""
This is '4-from_json_string' module.
Functions and Classes:
    from_json_string(my_str)
"""


def from_json_string(my_str):
    """ret python obj represented in JSON stirng"""
    from json import loads
    return loads(my_str)
