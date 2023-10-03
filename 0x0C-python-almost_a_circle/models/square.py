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

    def update(self, *args, **kwargs):
        """A method that updates the attributes"""
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key in ('id', 'size', 'x', 'y'):
                    setattr(self, key, value)

    def to_dictionary(self):
        '''A dictionary representation of a square'''
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
