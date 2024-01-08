#!/usr/bin/python3
"""
 function that returns True if the object is an instance of the class
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the \
            object is an instance of the class
            """
    if isinstance(obj, a_class):
        return True
    return False
