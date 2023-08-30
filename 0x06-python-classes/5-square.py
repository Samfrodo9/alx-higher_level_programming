#!/usr/bin/python3

"""A module that has a class with a private attribute"""


class Square():
    """A square class with a private attribute"""
    def __init__(self, size=0):
        """A method with a private attribute"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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

    def my_print(self):
        """A function  that prints # symbol"""
        for i in range(self.__size):
            if self.__size == 0:
                print()
                break
            print('#' * self.__size)
