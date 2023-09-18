#!/usr/bin/python3

"""A module that writes an Object to a text file using json"""


def save_to_json_file(my_obj, filename):
    """A function to do the above module documentation"""
    import json
    with open(filename, 'w', encoding='utf-8') as file:
        store = json.dumps(my_obj)
        file.write(store)
