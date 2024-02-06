#!/usr/bin/python3
"""
This is '4-inherits_from' module.
Functions and Classes:
    def inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    checking if object is instance of class that inherited
    (directly/indirectly) from specified class
    """
    related = issubclass(obj.__class__, a_class)
    not_same_class = (obj.__class__ is not a_class)

    return (related and not_same_class)
