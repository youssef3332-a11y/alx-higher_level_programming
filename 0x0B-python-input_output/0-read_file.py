#!/usr/bin/python
"""
module
.
"""
def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout."""
    with open(filename, encoding="utf-8") as file:
    print(file.read())
