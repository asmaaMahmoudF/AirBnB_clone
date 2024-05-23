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

    def do_create(self, arg):
        '''create a new instance of BaseModel'''
        arg = arg.split()
        classes = {
        'BaseModel': base_model.BaseModel,
        'User': user.User,
        'City': city.City,
        'Amenity': amenity.Amenity,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State
        }
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[arg[0]]()
        print(new_instance.id)
        new_instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
