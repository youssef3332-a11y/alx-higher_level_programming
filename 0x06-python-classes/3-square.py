#!/usr/bin/python3
"""for in silence there is no rejection"""


class Square:
    """you forget so easy"""
    def __init__(self, size=0):
        """ __init__"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """ area methode"""
        return self.__size ** 2