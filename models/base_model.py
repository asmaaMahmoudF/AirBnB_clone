#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        temp = {**self.__dict__}
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.updated_at.isoformat()
        temp["__class__"] = type(self).__name__
        return temp
    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__,self.id, self.__dict__)

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)