#!/usr/bin/python3
"""
This is '100-my_int' module.
Functions and Classes:
    class MyInt
"""


class MyInt(int):
    def __eq__(self, other):
        if self.real == other.real:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.real == other.real:
            return True
        else:
            return False
