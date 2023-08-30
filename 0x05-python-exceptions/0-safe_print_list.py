#!/usr/bin/python3
"""to print x element of a list"""


def safe_print_list(my_list=[], x=0):
    try:
        for a in range(0, x):
            print(f"{my_list[a]}", end="")
        print()

        return (x)
    except IndexError:
        b = 0
        for a in my_list:
            b = b + 1
        print()

        return (b)
