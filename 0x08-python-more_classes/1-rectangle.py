#!/usr/bin/python3
"""
a module:
learn more about classes
"""
class Rectangle:
    """
    Attributes:
    width: 
    height:
    Methodes:
    width: geter
    height: geter
    width: seter
    height: seter
    __init__: constracter
    """
    def __init__(self, width=0, height=0):
        """
        this:
        a constractor
        """
        self.height = height
        self.width = width
    @property
    def width(self):
        """
        retrive
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        setter

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    @property
    def height(self):
        """
        getter
        height
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        setter

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
