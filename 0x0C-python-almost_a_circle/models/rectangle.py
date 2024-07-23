# !/usr/bin/python3
"""
module
..
"""

from models.base import Base
class Rectangle(Base):
    """
    discreption
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        function discreption
        """
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)
    @property
    def width(self):
        """...."""
        return self.__width
    @width.setter
    def width(self, value):
        """...."""
        self.__width = value
    @property
    def height(self):
        """...."""
        return self.__height
    @height.setter
    def height(self, value):
        """...."""
        self.__height = value
    @property
    def x(self):
        """...."""
        return self.__x
    @x.setter
    def x(self, value):
        """...."""
        self.__x = value
    @property
    def y(self):
        """...."""
        return self.__y
    @y.setter
    def y(self, value):
        """...."""
        self.__y = value
r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)