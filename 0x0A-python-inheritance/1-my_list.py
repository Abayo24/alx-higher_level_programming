#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    def __init__(self, my_list=[]):
        """Initialize MyList with an optional list."""
        self.my_list = my_list

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
