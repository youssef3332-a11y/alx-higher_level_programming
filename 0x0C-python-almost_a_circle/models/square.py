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

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.validate_integer("width", value, False)
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """ update the attributes"""
        h = "_Rectangle__height"
        if args:
            list_attributes = list(self.__dict__.keys())
            del list_attributes[2]
            for i in range(len(args)):
                self.__dict__[list_attributes[i]] = args[i]
            self.__dict__[h] = self.__dict__["_Rectangle__width"]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    managed = "id"
                elif key == "size":
                    managed = "_Rectangle__width"
                else:
                    managed = "_Rectangle__{}".format(key)
                if managed in self.__dict__:
                    self.__dict__[managed] = value
            self.__dict__[h] = self.__dict__["_Rectangle__width"]
