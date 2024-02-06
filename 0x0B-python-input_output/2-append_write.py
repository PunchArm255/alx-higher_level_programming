#!/usr/bin/python3
"""
This is '2-append_write' module.
Functions and Classes:
    append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    append string to file then return num of char read
    """
    with open(filename, "a", encoding="UTF-8") as f:
        nc = f.write(text)

    return nc
