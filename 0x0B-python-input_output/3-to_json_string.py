#!/usr/bin/python3

"""A  module with a funcion that returns json rep of an object"""


def to_json_string(my_obj):
    """A function that serializes"""
    import json
    return json.dumps(my_obj)
