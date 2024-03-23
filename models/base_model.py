#!/usr/bin/python3
""" BaseModel """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel Class """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updated_at with the current datetime """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ dictionary containing all keys/values """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict


