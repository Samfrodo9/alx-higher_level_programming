#!/usr/bin/python3

"""
    A Rectangle Module defined here
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle: A class that defines a Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization of the instance of a rectangle """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id

        super().__init__(id)

    @property
    def width(self):
        """width getter for private attribute 'width' of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter for private attribute 'width' of rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter for private attribute 'height' of rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height setter for private attribute 'width' of rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter for private attribute 'x' of rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """x setter for private attribute 'width' of rectangle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter for private attribute 'y' of rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """y setter for private attribute 'width' of rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area calculates area of a rectangle

        Returns:
            int: area
        """
        return self.width * self.height

    def display(self):
        """
        display displays a symbol '#'
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        __str__ a method to a string representation of rectangle
        """
        rec = "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"
        return (rec.format(self.id, self.x, self.y, self.width, self.height))
    
    def update(self, *args):
        # Check the length of the args tuple
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        if len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        if len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        if len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
