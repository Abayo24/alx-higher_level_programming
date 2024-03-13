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

    def my_print(self):
        """prints square with char #"""
        if self.__size == 0:
            print("")
=======
        """Instantiation with optional size"""
        self.size = size

    @property
    def size(self):
        """Property to retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Property setter to set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with char #"""
>>>>>>> master
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
<<<<<<< HEAD
=======
        if self.__size == 0:
            print("")
>>>>>>> master
