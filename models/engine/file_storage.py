#!/usr/bin/python3

import json
from json.decoder import JSONDecodeError
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """The storage engine in AirBnB project"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary objects"""

        return __objects

    def new(self, obj):
        """sets in the __objects dictionary"""

        setattr(__objects, type(obj).__name__.id, obj)

    def save(self):
        """This method will serialize the __objects to json string"""

        json.dump(__objects,__file_path)

    def reload(self):
        """This method will deserialize the Json string to py dict"""

        if __file_path:
            __objects = json.load(__file_path)

