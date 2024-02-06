#!/usr/bin/python3
"""
This is '10-square' module.
Functions and Classes:
    class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """do a square bro"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
