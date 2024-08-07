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
    def area(self):
        """Returns area of a rectangle of a given `width` and `height`.

        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`

        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * (self.height - 1) + "#" * self.width)
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
    def __del__(self):
        print("Bye rectangle...")