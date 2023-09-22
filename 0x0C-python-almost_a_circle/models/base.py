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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''A method to save JSON string representation to a file'''
        if list_objs is None or len(list_objs) == 0:
            data = '[]'
        else:
            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            data = cls.to_json_string(dict_list)

        filename = cls.__name__ + '.json'
        with open(filename, encoding='utf-8', mode='w') as file:
            file.write(data)

        '''A method to save JSON string representation to a file        a = 0
        if issubclass(Base, list_objs):
            if list_objs is None or len(list_objs) == 0:
                a = 1
            filename = list_objs.__name__ + '.json'
            string = Base.to_json_string(list_objs)
            with open("filename", encoding='utf-8', mode='w') as file:
                if a == 1:
                    file.write('[]')
                else:
                    file.write(string)
        '''
