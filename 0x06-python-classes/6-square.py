#!/usr/bin/python3

"""A module that has a class with a private attribute"""


class Square():
    """A square class with a private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """A method with a private attribute"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (not isinstance(position, tuple) or (len(position) != 2) or not
                isinstance(position[0], int) or not
                isinstance(position[1], int)
                or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """A method that returns the area"""
        return int((self.__size) * (self.__size))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """ A method that set value for a tuple"""
        if type(value) == tuple and len(value) == 2 and \
                value[0] > 0 and value[1] > 0 and type(value[0]) == int\
                and type(value[1]) == int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """A function  that prints # symbol"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print((" " * self.__position[0]) + ('#' * self.__size))
