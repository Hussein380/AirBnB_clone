#!/usr/bin/python3
"""Define the Base Model Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represent the BaseModel of the HBnB project"""
    def __init__(self, *args, **kwargs):
        """initialize a new BaseModel
        Args:
            *args (any): unused
            **kwargs (dict): key/bvalue pairs of attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """update updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Retuens the dictionary of the BaseModels instance.
        includes the key/value pairs __class__ representing the
        class name of the object.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """Returns the print/str representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
