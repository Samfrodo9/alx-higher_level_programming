#!/usr/bin/python3

"""A module that defines a function to add args of a List"""


import sys
from os import path
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.isfile("add_item.json"):
    store = load_from_json_file("add_item.json")
else:
    store = []
for i in sys.argv[1:]:
    store.append(i)
save_to_json(store, "add_item.json")
