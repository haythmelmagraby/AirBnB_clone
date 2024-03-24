#!/usr/bin/python3
"""console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand consol class"""
    prompt = "(hbnb)"

    def emptyline(self):
        """dont execute anything"""
        pass

    def do_EOF(self, line):
        'EOF command to exit the program'
        return True

    def do_quit(self, line):
        'Quit command to exit the program'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
