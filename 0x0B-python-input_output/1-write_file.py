#!/usr/bin/python3

"""A Module that has a function that writes into a text file"""


def write_file(filename="", text=""):
    """A function that writes into a file"""
    with open(filename, mode='w', encoding='utf-8') as r:
        count = r.write(text)
    return count
