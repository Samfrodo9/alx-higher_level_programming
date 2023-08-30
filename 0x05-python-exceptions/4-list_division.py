#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for lis in range(list_length):
        try:
            newlist.append(my_list_1[lis] / my_list_2[lis])
        except TypeError:
            print("wrong type")
            newlist.append(0)
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0)
        except IndexError:
            print("out of range")
        finally:
            pass
    return newlist
