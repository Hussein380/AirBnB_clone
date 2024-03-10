#!/usr/bin/python3
""" Defines the HBnb console """

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """ Parse the command line input """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl

    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ Defines the HolbertonBnB command Interpreter.

    Attributes:
        prompt (str): The command prompt
    """

    prompt = "hbnb "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
    }

    def emptyline(self):
        """ Do nothing upon receiving an empty line """
        pass

    def default(self, arg):
        """Handle default behavior for cmd module when input is invalid """
        command_mappings = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }

        dot_match = re.search(r"\.", arg)
        if dot_match is not None:
            args_list = [arg[:dot_match.span()[0]], arg[dot_match.span()[1]:]]
            bracket_match = re.search(r"\((.*?)\)", args_list[1])
            if bracket_match is not None:
                command_args = [args_list[1][:bracket_match.span()[0]],
                                bracket_match.group()[1:-1]]
                if command_args[0] in command_mappings.keys():
                    command_call = "{} {}".format(args_list[0],
                                                  command_args[1])
                    return command_mappings[command_args[0]](command_call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """ Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """ Handle EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """ Create a new instance of a specified class and print its ID."""
        args_list = parse(arg)

        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """ Display the string representation of a class instance with
        given ID
        """
        args_list = parse(arg)
        obj_dict = storage.all()

        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args_list[0], args_list[1])])

    def do_destroy(self, arg):
        """ Delete a class instance with specified ID """
        args_list = parse(arg)
        obj_dict = storage.all()

        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1] not in obj_dict.keys()):
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args_list[0], args_list[1])]
            storage.save()

    def do_all(self, arg):
        """ display string representation of all instances of a given class
        or instantiated object"""
        args_list = parse(arg)

        if len(args_list) > 0 and args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(args_list) > 0 and \
                        args_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif not len(args_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """Retrieves the number of instances ofa given class """
        args_list = parse(arg)
        count = 0
        for obj in storage.all().values():
            if args_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """ Update a class instance with specified Id"""

        args_list = parse(arg)
        obj_dict = storage.all()

        if len(args_list) == 0:
            print("** class name missing **")
            return False

        if args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        if len(args_list) == 1:
            print("** instance id missing **")
            return False

        if "{}.{}".format(args_list[0], args_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False

        if len(args_list) == 2:
            print("** attribute name missing **")
            return False

        if len(args_list) == 3:
            try:
                type(eval(args_list[2])) != dict
            except NameError:
                print("** attribute name missing **")
                return False
        if len(args_list) == 4:
            obj = obj_dict["{}.{}".format(args_list[0], args_list[1])]
            if args_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args_list[2]])
                obj.__dict__[args_list[2]] = valtype(args_list[3])
            else:
                obj.__dict__[args_list[2]] = args_list[3]
        elif type(eval(args_list[2])) == dict:
            obj = obj_dict["{}.{}".format(args_list[0], args_list[1])]
            for k, v in eval(args_list[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
