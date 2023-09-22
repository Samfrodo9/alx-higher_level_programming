#!/usr/bin/python3
'''square module'''
Rectangle = __import__('models.rectangle').rectangle.Rectangle


class Square(Rectangle):
    '''a square class inherits from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor method'''
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''private instance method'''
        rec = "[Square] ({}) {:d}/{:d} - {:d}"
        return (rec.format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        '''size getter'''
        return (self.width)

    @size.setter
    def size(self, value):
        '''size setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        self.__size = value

#    def update(self, *args,)
