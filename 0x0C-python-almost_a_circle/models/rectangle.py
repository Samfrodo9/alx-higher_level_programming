#!/usr/bin/python3
from models.base import Base

"""
    A Rectangle Module
"""


class Rectangle(Base):
    """
    Rectangle A class that defines a Rectangle

    Args:
        Base (A class): Inherits from the Base Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ initialization of the instance of a rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id

        super().__init__(self.id)

        @property
        def width(self):
            """
            width getter for private attribute 'width' of rectangle

            Returns:
                int: width of rectangle
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            width setter for private attribute 'width' of rectangle

            Args:
                value (int): width of rectangle
            """
            self.__width = value

        @property
        def height(self):
            """
            height getter for private attribute 'height' of rectangle

            Returns:
                int: height of rectangle
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            height setter for private attribute 'width' of rectangle

            Args:
                value (int): height of rectangle
            """
            self.__height = value

        @property
        def x(self):
            """
            x getter for private attribute 'x' of rectangle

            Returns:
                int: x of rectangle
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            x setter for private attribute 'width' of rectangle

            Args:
                value (int): x of rectangle
            """
            self.__x = value

        @property
        def y(self):
            """
            y getter for private attribute 'y' of rectangle

            Returns:
                int: y of rectangle
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            y setter for private attribute 'width' of rectangle

            Args:
                value (int): y of rectangle
            """
            self.__y = value
