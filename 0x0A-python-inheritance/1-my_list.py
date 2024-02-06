#!/usr/bin/python3
"""
This is '1-my_list' module.
Functions and Classes:
    class MyList
"""


class MyList(list):
    """
    subclass who inherits from the 'list' class
    """
    def print_sorted(self):
        """print sorted tablo in an ascending order"""
        print(sorted(self))
