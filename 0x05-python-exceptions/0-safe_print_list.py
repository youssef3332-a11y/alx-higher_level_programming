#!/usr/bin/python3

# a function

def safe_print_list(my_list=[], x=0):
    test = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            test = i + 1
        except IndexError:
            break
    print("")
    return test
