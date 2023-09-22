#!/usr/bin/python3

"""A square class defined here"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square module that inherits from a Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        '''A constructor method'''
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__ A string rep of Square

        Returns:
                _type_: str
        """
        sqr = "[Square] ({}) {:d}/{:d} - {:d}"
        return (sqr.format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """width getter for private attribute 'width' of rectangle"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """width setter for private attribute 'width' of rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        self.__size = value
