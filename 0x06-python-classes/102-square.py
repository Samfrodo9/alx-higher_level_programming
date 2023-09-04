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

    def __lt__(self, right):
        """A function implementing < of a square"""
        if isinstance(right, Square):
            if (self.__size) * (self.__size) \
                    < (right.__size) * (right.__size):
                return True
            else:
                return False

    def __gt__(self, right):
        """A function implementing > of a square"""
        if isinstance(right, Square):
            if (self.__size) * (self.__size) \
                    > (right.__size) * (right.__size):
                return True
            else:
                return False

    def __ne__(self, right):
        """A function implementing != of a square"""
        if isinstance(right, Square):
            if (self.__size) * (self.__size) \
                    != (right.__size) * (right.__size):
                return True
            else:
                return False

    def __eq__(self, right):
        """A function implementing == of a square"""
        if isinstance(right, Square):
            if (self.__size) * (self.__size) \
                    == (right.__size) * (right.__size):
                return True
            else:
                return False

    def __ge__(self, right):
        """A function implementing >= of a square """
        if isinstance(right, Square):
            if (self.__size) * (self.__size) \
                    >= (right.__size) * (right.__size):
                return True
            else:
                return False

    def __le__(self, right):
        """A function implementing <= of a square"""
        return self.area() <= right.area()
