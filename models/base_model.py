#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

storage = models.storage


class BaseModel:
    """The base model class is the main class"""

    def __init__(self, *args, **kwargs):
        """The initialization method"""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid4())

        if kwargs:
            for key, value in kwargs.time():
                if key != __class__:
                    setattr(self, key, value)
            if "created_at" or "updated_at" in kwargs:
                self.created_at = \
                    datetime.\
                    strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                self.updated_at = \
                    datetime.\
                    strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        storage.new(self)

    def save(self):
        """Update the time of instance creation"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """A function to collect the needed data and put them into dic
        by making a copy of __dict__ using {**self}"""

        temp = {**self.__dict__}
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.updated_at.isoformat()
        temp["__class__"] = type(self).__name__
        return temp

    def __str__(self):
        """overriding the __str__ method to print specific format"""
        return \
            "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
