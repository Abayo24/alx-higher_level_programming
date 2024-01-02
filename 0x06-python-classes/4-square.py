#!/usr/bin/python3
"""Size validation"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Instantiation with size"""
        self.__size = size

    def area(self):
        """area of square method"""
        return (self.__size)**2

    @property
    def size(self):
        """getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
