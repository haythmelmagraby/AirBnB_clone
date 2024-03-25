#!/usr/bin/python3
"""Storage Module"""
import json
import os
import datetime


class FileStorage:
    """ file storage class """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """sets in __objects the obj"""
        obj_cn = obj.__class__.__name__
        the_key = "{}.{}".format(obj_cn, obj.id)
        FileStorage.__objects[the_key] = obj

    def all(self):
        """the dictionary __objects"""
        return FileStorage.__objects

    def save(self):
        """serializes __objects to the JSON file"""
        objs = FileStorage.__objects
        my_dict = {}
        for obj in objs.keys():
            my_dict[obj] = objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    my_dict = json.load(f)
                    for key, value in my_dict.items():
                        if ',' in key:
                            cn, o = key.split(',')
                            cl = eval(cn)
                            inst = cl(**value)
                            FileStorage.__objects[key] = inst
        except FileNotFoundError:
            pass
