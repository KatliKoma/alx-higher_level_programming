#!/usr/bin/python3

"""
module for class Rectangle
"""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialized class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getWidth"""
        return self.__width

    @width.setter
    def width(self, widthValue):
        """setWidth"""
        if type(widthValue) != int:
            raise TypeError("must be an integer")
        if widthValue < 0:
            raise ValueError("width must be greater than equal to 0")
        self.__width = widthValue

    @property
    def height(self):
        """getHeight"""
        return self.__height

    @height.setter
    def height(self, HeightValue):
        """setHeight"""
        if type(HeightValue) != int:
            raise TypeError("must be an integer")
        if HeightValue < 0:
            raise ValueError("height must be greater than equal 0")
        self.__height = HeightValue

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2
