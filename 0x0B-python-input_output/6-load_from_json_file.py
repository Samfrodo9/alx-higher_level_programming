#!/usr/bin/python3

""""A module that creates Object from a 'Json file'"""


def load_from_json_file(filename):
    """A function that creates Object from a Json file"""
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        contents = ""
        for words in file:
            contents = contents + words
        return json.loads(contents)
