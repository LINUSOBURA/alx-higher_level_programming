#!/usr/bin/python3
"""Base Module"""
import json


class Base:
    """Base classused to track the id to avoid duplicates"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Funcion to convert dictionary to Json string"""
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of instances to a file in JSON format"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(list_dict)
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Converts from Json String to dictionary"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a file and return a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                data = f.read()
                if not data:
                    return []
                else:
                    list_dict = cls.from_json_string(data)
                    return [cls.create(**obj) for obj in list_dict]
        except FileNotFoundError:
            return []
