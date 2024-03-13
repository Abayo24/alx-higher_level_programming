#!/usr/bin/python3
<<<<<<< HEAD
"""Size validation"""
=======
"""Square with size"""
>>>>>>> master


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
<<<<<<< HEAD
        """Instantiation with size"""
        if not isinstance(size, int):
=======
        """Instantiation with optional size"""
        if type(size) != int:
>>>>>>> master
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
<<<<<<< HEAD
        """area of square method"""
        return (self.__size)**2
=======
        """Public instance method that returns the current square area"""
        return self.__size ** 2
>>>>>>> master
