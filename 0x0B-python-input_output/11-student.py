#!/usr/bin/python3

"""
    A module that has a function that
     retrieves a dictionary representation
     of a student class
"""


class Student():
    '''A class that defines a student'''

    def __init__(self, first_name, last_name, age):
        '''An initialization of public attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            A function that retrieves a dict
             representation of a student class
        '''
        if type(attrs) is not list:
            return (self.__dict__)

        new = True
        for element in attrs:
            if type(element) != str:
                new = False
        if new:
            dict_ = {}
            for attr in attrs:
                if attr in self.__dict__:
                    dict_[attr] = self.__dict__[attr]
            return (dict_)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        '''A method that replaces all attributes of the student instance'''
        self.__dict__.update(json)
        # We may also say self.__dict__ = json, but for one check failed
