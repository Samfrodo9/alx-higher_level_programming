#!/usr/bin/python3

"""A module that has a function that apppends to a file"""


def append_write(filename='', text=''):
    """A function that appends to a file"""
    with open(filename, mode='a', encoding='utf-8') as file:
        appended = file.write(text)
    return appended
