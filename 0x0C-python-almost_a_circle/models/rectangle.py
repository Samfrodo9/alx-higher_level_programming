#!/usr/bin/python3

"""
    A Rectangle Module defined here
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle: A class that defines a Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization of the instance of a rectangle """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id

        super().__init__(id)

        @property
        def width(self):
            """width getter for private attribute 'width' of rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """width setter for private attribute 'width' of rectangle"""
            self.__width = value

        @property
        def height(self):
            """
            height getter for private attribute 'height' of rectangle
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            height setter for private attribute 'width' of rectangle
            """
            self.__height = value

        @property
        def x(self):
            """x getter for private attribute 'x' of rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            """x setter for private attribute 'width' of rectangle"""
            self.__x = value

        @property
        def y(self):
            """ y getter for private attribute 'y' of rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            """y setter for private attribute 'width' of rectangle"""
            self.__y = value
