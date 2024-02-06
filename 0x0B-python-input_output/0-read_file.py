#!/usr/bin/python3
"""
This is '0-read_file' module.
Functions and Classes:
    read_file(filename="")
"""


def read_file(filename=""):
    """check content of file then print to stdoutput"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
