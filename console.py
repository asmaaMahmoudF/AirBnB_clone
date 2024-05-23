#!/usr/bin/python3
'''
    implementing the console class
'''

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import amenity
from models.place import Place
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Simple command processor.  """

    prompt = '(hbnb)'

    classes = {
        'BaseModel': BaseModel.BaseModel,
        "User": User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity':amenity.Amenity,
        'Review': Review,
        'State': State,
        'City': City,
    }

    def do_update(self, arg):
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''exit the cmd iteration'''
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it'''
        args_list = arg.split()
        classes = {
        'BaseModel': BaseModel.BaseModel,
        "User": User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity':amenity.Amenity,
        'Review': Review,
        'State': State,
        'City': City
       }
        if len(args_list) > 1:
            print(f"unknown number of args {args}")
            print(f"Usage: create <class-name>")
        elif len(args_list) == 0:
            print('** class name missing **')
        elif args_list[0] not in classes.keys():
            print('** class doesn\'t exist **')
        else:
            instance = classes[args_list[0]]()
            print(instance.id)
            instance.save()

    def do_show(self, arg):
        return True

    def do_destroy(self, arg):
        pass

    def do_all(self, arg):
        pass

    def do_help(self, arg):
        return super().do_help(arg)

    def help_EOF(self):
        print("EOF signal to exit the program.")

    def help_quit(self):
        print("Quit command to exit the program.")   

if __name__ == '__main__':
    HBNBCommand().cmdloop()
