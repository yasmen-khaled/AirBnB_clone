#!/usr/bin/python3
"""Modules"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """filestorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all fun  selected all objects"""

        return FileStorage.__objects

    def new(self, obj):
        """new  creating a new object to __object dict"""

        new_entry = obj.__class__.__name__ + '.' + obj.id

        FileStorage.__objects[new_entry] = obj

    def save(self):
        """save Serializeing from py to jso"""

        creat_dict = {

            obj: FileStorage.__objects[obj].to_dict()
            for obj in FileStorage.__objects.keys()
            }

        with open(FileStorage.__file_path, 'w') as output:
            json.dump(creat_dict, output)

    def reload(self):
        """reloading  Deserializeing from json to py"""

        if FileStorage.__file_path is None:
            return
        try:
            with open(FileStorage.__file_path) as x:
                if os.path.getsize(FileStorage.__file_path) == 0:
                    return
                creat_dict = json.load(x)
                for key in creat_dict.values():
                    class_name = key["__class__"]
                    del key["__class__"]

                    self.new(eval(class_name)(**key))
        except FileNotFoundError:
            return
