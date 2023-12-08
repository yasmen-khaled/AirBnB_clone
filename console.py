#!/usr/bin/python3
"""Modules"""
import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class for consolo in airbnb"""

    prompt = "(hbnb) "
    __cl = {
            "Review",
            "Place",
            "State",
            "User",
            "BaseModel",
            "Amenity",
            "City"
            }

    def do_EOF(self, lin):
        """EOF command to exit the program"""

        print('')
        return True

    def do_quit(self, lin):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """do nothing"""

        pass

    def do_create(self, lin):
        """to create"""

        firs = lin.split()
        if len(firs) == 0:
            print("** class name missing **")
        elif firs[0] not in HBNBCommand.__cl:
            print("** class doesn't exist **")
        else:
            print(eval(firs[0])().id)
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
