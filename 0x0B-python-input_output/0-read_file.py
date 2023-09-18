#!/usr/bin/python3

"""A Module that has a function that reads a text file"""


def read_file(filename=""):
    """A function that reads a file"""
    with open(filename, mode='r', encoding='utf-8') as r:
        for i in r:
            print(i, end="")
