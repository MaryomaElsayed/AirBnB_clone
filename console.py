#!/usr/bin/env python3
""" Main script for the HBnB console.
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ HBnBCommand class defines a command-line 
    interpreter for object management and storage.
    """

    my_models = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review}

    prompt = "(hbnb) "
    models = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"]

    def do_quit(self, args):
        """ Quit command to exit the program.\n
        """
        quit()

    def do_EOF(self, args):
        """ End Of File command to exit the program.\n
        """
        quit()

    def emptyline(self):
        """ Do nothing on empty line\n
        """
        pass

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""

        all_data = storage.all()
        my_data = []
        if args not in HBNBCommand.my_models:
            print("** class doesn't exist **")
            return
        if args in self.models:
            for key, value in all_data.items():
                if args in key:
                    split_str = key.split(".")
                    new_str = "[" + split_str[0] + "]"\
                        + " (" + split_str[1] + ")"
                    my_data.append(new_str + " " + str(value))
                    print(my_data)

    def do_show(self, args):
        """ Print the string representation of an instance.
        """
        print("Show ...!")
        pass

    def do_create(self, args):
        """ Create a new instance of a specified class.
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.my_models:
            print("** class doesn't exist **")
            return
        else:
            new_object = eval(args[0])()
            new_object.save()
            print(new_object.id)

    def do_update(self, args):
        """ Update an instance based on the class name.
        """
        print("Update ...!")
        pass

    def do_destroy(self, args):
        """ Delete an instance.
        """
        print("Delete ...!")
        pass

    def do_count(self, args):
        """ Count the number of instances of a class.
        """
        print("Count ...!")
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
