#!/usr/bin/python3
"""
A class Square that defines a square by: (based on 2-square.py)
"""


class Square():
    """
    This is a class Square
    """

    def __init__(self, size=0):
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif (size < 0):
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)
