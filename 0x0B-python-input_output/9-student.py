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

    def to_json(self):
        '''
            A function that retrieves a dict
             representation of a student class
        '''
        return (self.__dict__)
