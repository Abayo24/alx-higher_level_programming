#!/usr/bin/python3
<<<<<<< HEAD
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
=======
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a size of the square
        __position (tuple): position of the square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): positoin of the square in 2D space
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
>>>>>>> master
        return self.__size

    @size.setter
    def size(self, value):
<<<<<<< HEAD
        """setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
=======
        """setter of __size
        Args:
            value (int): size of a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
>>>>>>> master

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
<<<<<<< HEAD
        """getter method for position"""
=======
        """getter of __position
        Returns:
            The position of the square in 2D space
        """
>>>>>>> master
        return self.__position

    @position.setter
    def position(self, value):
<<<<<<< HEAD
        """setter method for position"""
        if (not isinstance(value, tuple)) or (len(value) != 2) or \
           (not isinstance(value[0], int)) or (value[0] < 0) or \
           (not isinstance(value[1], int)) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 \
                       positive integers")
=======
        """setter of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
>>>>>>> master
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
