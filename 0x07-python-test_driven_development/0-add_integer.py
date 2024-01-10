#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """function that adds 2 integers."""
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError("a must be an integer or b must be an integer")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
