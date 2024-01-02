#!/usr/bin/python3
"""Size validation"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Instantiation with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area of square method"""
        return (self.__size)**2
