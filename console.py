#!/usr/bin/python3
'''
    implementing the console class
'''

import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Simple command processor.  """

    prompt = '(hbnb)'

    classes = {
        'BaseModel': BaseModel,
        "User": User,
        'Place': Place,
        'State': State,
        'City': City,
        'Review': Review,
        'State': State,
        'City': City,
    }

    def do_EOF(self, arg):
        '''exit the cmd iteration'''
        return True

    def do_help(self, arg):
        return super().do_help(arg)

    def do_quit(self, arg):
        return True

    def help_quit(self):
        '''help the quit command'''
        print("Quit command to exit the program.")

    def emptyline(self):
        '''do nothing when an empty line is entered'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
