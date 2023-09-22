#!/usr/bin/python3

"""A square class defined here"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square module that inherits from a Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__ A string rep of Square

        Returns:
                _type_: str
        """
        sqr = "[Square] ({}) {:d}/{:d} - {:d}"
        return (sqr.format(self.id, self.x, self.y, self.size))
