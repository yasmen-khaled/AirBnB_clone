#!/usr/bin/python3
"""Modules"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for consolo in airbnb"""

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
