#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage():
   

    __file_path = "file.json"
    __objects = {}

    """______ all - method  selected all objects _______"""
    def all(self):

        return FileStorage.__objects
    
    """______ new - method  creating a new  object to __object dict _______"""

    def new(self, obj):

        new_entry = obj.__class__.__name__ + '.' + obj.id

        FileStorage.__objects[new_entry] = obj
 
    """______ save - Serializeing converting from py to json _______"""

    def save(self):
    
        creat_dict = {
    
            obj: FileStorage.__objects[obj].to_dict()
            for obj in FileStorage.__objects.keys()

            }
        
        with open(FileStorage.__file_path, 'w') as x:
            json.dump(creat_dict, x)

        """______reloading - Deserializeing converting from json to py _______"""

    def reload(self):

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
