#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents base Model of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if length(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "created_at" or m == "updated_at":
                    self.__dict__[m] = datetime.strptime(n, tformat)
                else:
                    self.__dict__[m] = n
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        redict = self.__dict__.copy()
        redict["created_at"] = self.created_at.isoformat()
        redict["updated_at"] = self.updated_at.isoformat()
        redict["__class__"] = self.__class__.__name__
        return redict

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
