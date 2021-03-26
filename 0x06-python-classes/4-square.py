#!/usr/bin/python3
"""
A class Square that defines a square by: (based on 3-square.py)
"""


class Square():
    """
    This is a class Square
    """

    def __init__(self, size):
        if type(size) != int:
            print("size must be an integer", end=" ")
            raise TypeError
        elif (size < 0):
            print("size must be >= 0", end=" ")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(self.__size) != int:
            print("size must be an integer", end=" ")
            raise TypeError
        elif (value < 0):
            print("size must be >= 0", end=" ")
            raise ValueError
        else:
            self.__size = value
