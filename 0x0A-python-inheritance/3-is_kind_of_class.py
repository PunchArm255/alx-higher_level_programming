#!/usr/bin/python3
"""
This is '3-is_kind_of_class' module.
Functions and Classes:
    def is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    checking if an object is instance of class (exact/inherited)
    or not
    """
    return isinstance(obj, a_class)
