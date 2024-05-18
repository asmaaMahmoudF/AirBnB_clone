#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
     
    prompt = '(hbnb)'
 
    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        pass

    def do_show(self, arg):
        pass

    def do_destroy(self, arg):
       pass

    def do_all(self, arg):
        pass 

if __name__ == '__main__':
    HBNBCommand().cmdloop()