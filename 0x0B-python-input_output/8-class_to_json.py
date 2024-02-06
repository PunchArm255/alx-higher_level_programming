#!/usr/bin/python3
"""
This is '8-class_to_json' module.
Functions and Classes:
    class_to_json(obj)
"""


def class_to_json(obj):
    """
    ret dict desc for JSON serial of obj
    """
    my_dict = {}
    for item in dir(obj):
        if (not item.startswith("__")) and (not callable(getattr(obj, item))):
            my_dict[item] = getattr(obj, item)

    return my_dict
