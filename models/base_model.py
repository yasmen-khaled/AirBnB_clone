#!/usr/bin/python3
"""Modules."""
import uuid as u
import datetime as d


class BaseModel:
    """class base modle first class the parent
        in this project
    """

    def __init__(self, *args, **kwargs):
        """init function the main function"""

        self.id = str(u.uuid4())
        self.created_at = d.datetime.today()
        self.updated_at = d.datetime.today()
        sf = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = d.datetime.strptime(value, sf)
                else:
                    self.__dict__[key] = value

    def save(self):
        """save function to update the updated"""

        self.updated_at = d.datetime.today()

    def to_dict(self):
        """to_dict restore the dict by created
        and updated + class(name)
        """

        re_dict = self.__dict__.copy()
        re_dict["__class__"] = self.__class__.__name__
        re_dict["created_at"] = self.created_at.isoformat()
        re_dict["updated_at"] = self.updated_at.isoformat()
        return re_dict

    def __str__(self):
        """str the function format"""

        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
