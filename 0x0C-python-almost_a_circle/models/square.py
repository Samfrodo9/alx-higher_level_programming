#!/usr/bin/python3
"""The square model, let's write"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square module that inherits from a Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        '''A constructor method'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter for Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter for Square."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ A string rep of Square

        Returns:
                _type_: str
        """
        sqr = "[Square] ({}) {:d}/{:d} - {:d}"
        return sqr.format(self.id, self.x, self.y, self.size)
