#!/usr/bin/python3
"""Size validation"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size"""
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        """getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method for position"""
        if (not isinstance(value, tuple)) or (len(value) != 2) or \
           (not isinstance(value[0], int)) or (value[0] < 0) or \
           (not isinstance(value[1], int)) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 \
                       positive integers")
        else:
            self.__position = value

    def __str__(self):
        """String representation of a Square instance
        Returns:
            Formatted string representing the square
        """
        if self.size == 0:
            return ""
        string = "\n" * self.position[1] + (" " * self.position[0] +
                                            "#" * self.size + "\n") * self.size
        return string[:-1]
