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

    Attributes:
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
        oclass_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oclass_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file """
        odict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                keys_to_delete = []
                for o in obj_dict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name) (**o))
        except FileNotFoundError:
            return
