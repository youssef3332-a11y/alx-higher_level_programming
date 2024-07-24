#!/usr/bin/python3
"""
module
..
"""
import json


class Base:
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """save to file"""
        import json
        json = to_json_string(list_objs)
        name = "{}.json".format(cls)
        with open(name, "w") as f:
            f.write(json)
