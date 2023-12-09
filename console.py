#!/usr/bin/python3
"""Modules"""
import cmd
import models
from models import storage
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

        """__show - print class name and id___"""

    def do_show(self, lin):

        _str = lin.split()
        if not lin:
            print("** class name missing **")
            return
        elif not self.do_check(_str[0]):
            return
        elif len(_str) < 2:
            print("** instance id missing **")
            return

        _object = _str[0] + '.' + _str[1]
        _dict = storage.all()

        if _object not in _dict:
            print("** no instance found **")
            return
        else:
            print(_dict[_object])

    def do_destroy(self, lin):

        _str = lin.split()
        if not lin:
            print("** class name missing **")
            return
        elif not self.do_check(_str[0]):
            return
        elif len(_str) < 2:
            print("** instance id missing **")
            return

        _object = _str[0] + '.' + _str[1]
        _dict = storage.all()

        if _object not in _dict:
            print("** no instance found **")
            return
        else:
            if _dict[_object] is not None:
                del _dict[_object]
                storage.save()

    def do_check(self, class_name):
        """__checks if the class name is exist in the __cl__"""

        if class_name not in HBNBCommand.__cl:
            print("** class doesn't exist **")
            return False
        return True

    def do_all(self, lin):
        """print all"""

        ar = lin.split()
        ob = storage.all()
        if len(ar) != 0:
            if ar[0] not in HBNBCommand.__cl:
                print("** class doesn't exist **")
                return
            else:
                lis = []
                for k in storage.all():
                    if ar[0] == ob[k].__class__.__name__:
                        lis.append(str(ob[k]))
        else:
            for k in ob:
                lis.append(str(ob[k]))
        print(lis)

        """_______Updates class name and id__________"""
    def do_update(self, arg):
        
        _list = []
        duble_qout = False
        _inp = ""

        for ch in arg:
            if ch == ' ' and not duble_qout:
                _list.append(_inp)
                _inp = ""
            elif ch == '"':
                duble_qout = not duble_qout
            else:
                _inp += ch

        if _inp:
            _list.append(_inp)

        if len(_list) < 1:
            print("** class name missing **")
        elif not self.do_check(_list[0]):
            return
        elif len(_list) < 2:
            print("** instance id missing **")
        elif len(_list) < 3:
            print("** attribute name missing **")
        elif len(_list) < 4:
            print("** value missing **")
        else:
            _object = "{}.{}".format(_list[0], _list[1])
            if _object in storage.all():
                storage.save()
            else:
                print("** no instance found **")
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
