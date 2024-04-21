#!/usr/bin/python
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        sys.stderr.write("Exception: {}".format(error))
        return False
