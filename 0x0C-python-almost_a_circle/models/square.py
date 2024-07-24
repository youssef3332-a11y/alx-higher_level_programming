#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class
    ...
    """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding __str__ of rectangle"""
        result = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        result += "{}/{} - ".format(self.x, self.y)
        result += "{}".format(self.height)
        return result
