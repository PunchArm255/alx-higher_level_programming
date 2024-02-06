#!/usr/bin/python3
"""
This is '7-base_geometry' module.
Functions and Classes:
    class BaseGeometry
"""


class BaseGeometry():
    """geo class"""
    def area(self):
        """spawn excep"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """make sure that value is int"""
        if type(value) not in [int, float]:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
