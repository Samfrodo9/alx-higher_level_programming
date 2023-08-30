#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    1) Get the length of the list
    2) Iterate through the list
    3) Print only integers and skip others
    4) If x > len(list), raise IndexError
    5) Try and except must be used
    6) Return number of integers printed
    """
    size = len(my_list)  # Get the length of the list
    
    ReturnValue = 0
    try:
        if x <= size:
            for y in range(0, x):
                if type(my_list[y]) is int:
                    print("{:d}".format(my_list[y]), end="")
                    ReturnValue = ReturnValue + 1
                else:
                    continue

            print()  # Print a new line after printing the integers
            return ReturnValue
        else:
            raise IndexError  # Raise IndexError when x > size

    except TypeError:
        pass

# Test the function
my_list = [1, 2, 3, 'hello', 4, 5]
x = 10  # Choose the number of integers you want to print

result = safe_print_list_integers(my_list, x)
print("Number of integers printed:", result)

