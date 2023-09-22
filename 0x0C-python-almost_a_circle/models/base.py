#!/usr/bin/python3

"""
    A module that defines a class
"""
import json
dumps = json.dumps
loads = json.loads


class Base:
    """
    A class that creates an ID
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''A method that returns JSON rep of a list_dictionaries'''
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return dumps(list_dictionaries)

