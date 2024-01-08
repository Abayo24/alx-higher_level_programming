#!/usr/bin/python3
"""
function that returns the list of available \
        attributes and methods an object
"""


def lookup(obj):
    """returns list object"""
    if isinstance(obj, object):
        return dir(obj)
