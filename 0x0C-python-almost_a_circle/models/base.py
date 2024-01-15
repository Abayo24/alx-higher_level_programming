#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """first class Base"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep of list_objs to a file"""
        if list_objs is None:
            return "[]"
        else:
            filename = cls.__name__ + ".json"
            with open(filename, "w") as f:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return list()
        else:
            return json.loads(json_string)
