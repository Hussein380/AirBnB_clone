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
        arg_list = [arg[:dot_match.span()[0]], arg[dot_match.span()[1]:]]
        bracket_match = re.search(r"\((.*?)\)", arg_list[1])
        if bracket_match is not None:
            command_args = [arg_list[1][:bracket_match.span()[0]],
                            bracket_match.group()[1:-1]]
            if command_args[0] in command_mappings.keys():
                command_call = "{} {}".format(arg_list[0], command_args[1])
                return command_mappings[command_args[0]](command_call)

    print("*** Unknown syntax: {}".format(arg))
    return False
