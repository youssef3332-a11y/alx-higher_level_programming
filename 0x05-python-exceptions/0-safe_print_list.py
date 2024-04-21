#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        test = 0
        for i in range(x):
            print(mylist[i], end="")
            test = i
        print()
    except Exception:
        return test
