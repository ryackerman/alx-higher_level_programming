#!/usr/bin/python3
"""
Defines the Base class
"""
import json


class Base:
    """
    Base class for managing id attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init a Base instance
        Args:
            id (int): Optional. The id value for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        json_string = "[]"
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance
    
    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                instances = [cls.create(**dict) for dict in list_dicts]
                return instances
        except FileNotFoundError:
            return []
        
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    def to_dictionary(self):
        """Returns the dictionary representation of a Base instance"""
        attrs = ["id"]
        if hasattr(self, "size"):
            attrs.extend(["size", "x", "y"])
        else:
            attrs.extend(["width", "height", "x", "y"])
        return {attr: getattr(self, attr) for attr in attrs}
