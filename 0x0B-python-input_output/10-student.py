#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student"""
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {k: getattr(self, k) for k in attrs
                    if hasattr(self, k)}
        return self.__dict__
