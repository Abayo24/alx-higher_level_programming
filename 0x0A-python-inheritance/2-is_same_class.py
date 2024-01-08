#!/usr/bin/python3
"""
 function that returns True if the object is an instance of the class
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a given class.

    Args:
    - obj: The object to be checked.
    - a_class: The class to check against.

    Returns:
    - True if obj is an instance of a_class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
