#!/usr/bin/python3
"""
This is '0-lookup' module.
Functions and Classes:
    def lookup(obj)
"""


def lookup(obj):
    """
    returns list of dispo attributes/methods of object
    """
    return dir(obj)
