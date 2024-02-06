#!/usr/bin/python3
"""
This is '1-write_file' module.
Functions and Classes:
    write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    write string to file then return num of char done
    """
    with open(filename, "w", encoding="UTF-8") as f:
        nc = f.write(text)

    return nc
