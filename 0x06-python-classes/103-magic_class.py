#!/usr/bin/python3

"""A magic class"""

import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius):
        """Initializes the Magic Class"""

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of the magic class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the Magic Class"""
        return (2 * math.pi * self.__radius)
