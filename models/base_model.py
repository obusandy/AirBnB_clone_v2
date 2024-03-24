#!/usr/bin/python3
"""Define the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ 
        Starts a new Base model
    """
    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for sk, ks in kwargs.items():
                if sk == "created_at" or sk == "updated_at":
                    self.__dict__[sk] = datetime.strptime(ks, tform)
                else:
                    self.__dict__[sk] = ks
        else:
            models.storage.new(self)

        """ 
            sets current date time
        """

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
       
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

        """ 
            return base model instance
        """

    def __str__(self):
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
