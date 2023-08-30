#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    1) we'll get the length of the list
    2) We use length got to iterate the list
    3) We set a condition to print only integers and skip others
    4) If x > len(list), raise IndexError
    5) Try and except must be used
    6) Return No. of integers printed
    """
    size = 0
    for length in my_list:
        size = size + 1

    ReturnValue = 0
    try:
        for y in range(0, x):
            if type(my_list[y]) is int:
                print("{:d}".format(my_list[y]), end="")
                ReturnValue = ReturnValue + 1
            else:
                continue

        print()
        return ReturnValue

    except IndexError:
        pass
