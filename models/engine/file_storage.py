#!/usr/bin/python3
"""Defines the FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage systems

    Attributes;
        __file_path (str): The name of the file to save objects to
        __objects (dict): A dictionary of instantiated objects.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary of all objects """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new objects to __objects."""
        obj_key = "{} {}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serialize __objects to the JSON file """
        serialize_objects = {
                key: obj.to_dict() for key, obj in
                FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialize_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists """
        try:
            with open(FileStorage.__file_path) as file:
                serialized_objects = json.load(file)
                for key, obj in serialized_objects.items():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
