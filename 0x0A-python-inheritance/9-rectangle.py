#!/usr/bin/python3
"""
This is '9-rectangle' module.
Functions and Classes:
    class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """do a reccy lollol"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate surf of a reccy"""
        return self.__width * self.__height

    def __str__(self):
        """txt reppy of reccy"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
