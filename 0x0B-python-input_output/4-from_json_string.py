#!/usr/bin/python3

"""A module that returns an object representation of a JSON string"""


def from_json_string(my_str):
    '''A function that deserializes an object'''
    import json
    return json.loads(my_str)
