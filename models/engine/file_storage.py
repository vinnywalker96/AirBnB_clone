#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json


class FileStorage:
    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, "w") as f:
            json_obj = {key: obj.to_dict() for key, obj
                        in self.__objects.items()}
            json.dump(json_obj, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)
            for key, value in json_obj.items():
                obj = eval(value['__class__'])(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            return
