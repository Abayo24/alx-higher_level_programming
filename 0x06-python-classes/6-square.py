#!/usr/bin/python3
<<<<<<< HEAD
"""Size validation"""
=======
"""Square with size"""
>>>>>>> master


class Square:
    """Representation of a square"""

    def __init__(self, size=0, position=(0, 0)):
<<<<<<< HEAD
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
=======
        """Instantiation with optional size and optional position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property to retrieve size"""
        return (self.__size)

    @size.setter

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property to retrieve position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Property setter to set position"""
        if ((type(value) != tuple) or (len(value) != 2) or
                (type(value[0]) != int) or (value[0] < 0) or
                (type(value[1]) != int) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2
>>>>>>> master

    def my_print(self):
        """Public instance method that prints the square with char #"""
        if self.__size == 0:
            print("")
            return
        "Not empty (size != 0)"
        for new_line in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
<<<<<<< HEAD
=======
     def my_print(self):
        """Public instance method that prints the square with char #"""
        if self.__size == 0:
            print("")
            return
        "Not empty (size != 0)"
        for new_line in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
>>>>>>> master
            print("")
