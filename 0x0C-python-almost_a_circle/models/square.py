#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set size of square"""
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, 
                self.y, self.width)

    def update(self, *args, **kwargs):
        """updates all attributes"""
        if len(args) > 0 and args:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
