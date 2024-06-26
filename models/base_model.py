#!/usr/bin/python3
""" BaseModel """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ BaseModel Class """
    def __init__(self, *args, **kwargs):
        tf = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                elif key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.strptime(value, tf))
                else:
                    continue
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updated_at with the current datetime """
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ dictionary containing all keys/values """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        if isinstance(base_dict["created_at"], datetime):
            base_dict["created_at"] = self.created_at.isoformat()
        if isinstance(base_dict["updated_at"], datetime):
            base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
