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
=======
        """Instantiation with optional size"""
>>>>>>> master
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
