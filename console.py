#!/usr/bin/python3
"""console module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand consol class"""
    prompt = "(hbnb)"
    classes = {"BaseModel":BaseModel}

    def emptyline(self):
        """dont execute anything"""
        pass

    def do_EOF(self, line):
        'EOF command to exit the program'
        return True

    def do_quit(self, line):
        'Quit command to exit the program'
        return True

    def do_create(self, line):
        'Creates a new instance of BaseModel'
        if line not in self.classes:
            print("** class doesn't exist **")
        elif line is None or line == "":
            print("** class name missing **")
        elif line in self.classes:
            new_ins = self.classes[line]()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, line):
        'Prints the string'
        if line is None or line == "":
            print("** class name missing **")
        else:
            splitted = line.split(' ')
            if splitted[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(splitted) < 2:
                print("** instance id missing **")
            else:
                result = "{}.{}".format(splitted[0], splitted[1])
                if result in storage.all():
                    print(storage.all()[result])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        'Deletes an instance based on the class name'
        return True

    def do_all(self, line):
        'Prints all string representation of all instances'
        return True

    def do_update(self, line):
        'Updates an instance based on the class name'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
