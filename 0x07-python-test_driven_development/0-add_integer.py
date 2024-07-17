#!/usr/bin/python3
"""
module for adding integers
"""
def add_integer(a, b=98):
    """adds two integers.
    Args:
        a: integer or float
        b: integer or float , =98 by default
    Raises:
        TypeError: if a, b are not int or float.
    Returns:
        the sum of the two integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")