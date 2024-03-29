#!/usr/bin/python3
"""add a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
