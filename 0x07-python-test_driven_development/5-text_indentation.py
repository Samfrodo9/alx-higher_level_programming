#!/usr/bin/python3

"""A module that prints a text with 2 new lines after some special chrs"""


def text_indentation(text):
    """A function that prints and indents a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for words in text:
        if words == "":
            continue
        else:
        print(words, end="")
        if words in ('.', '?', ':'):
            print('\n')
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
