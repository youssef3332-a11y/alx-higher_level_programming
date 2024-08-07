#!/usr/bin/python3
'''Module for Rectangle class.'''

from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """calculate the area"""
        return self.width * self.height

    def display(self):
        """display with #"""
        result = (' ' * self.x + '#' * self.width + '\n') * self.height
        print('\n' * self.y, end='')
        print(result, end='')

    def __str__(self):
        """overriding __str__"""
        result = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        result += "{}/{} - ".format(self.x, self.y)
        result += "{}/{}".format(self.width, self.height)
        return result

    def update(self, *args, **kwargs):
        """ update the attributes"""
        if args:
            list_attributes = list(self.__dict__.keys())
            for i in range(len(args)):
                self.__dict__[list_attributes[i]] = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    managed = "id"
                else:
                    managed = "_Rectangle__{}".format(key)
                if managed in self.__dict__:
                    self.__dict__[managed] = value

    def to_dictionary(self):
        """ to dictionary"""
        dic = {}
        for key, value in self.__dict__.items():
            list = key.split('__')
            dic[list[-1]] = value
        return dic
