#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """The storage engine in AirBnB project"""

    __file_path: str = "file.json"
    __objects: dict = {}

    def __init__(self):
        """The initialization method (Constructor)"""
        pass

    def all(self):
        """Return the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in the __objects dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects stored and persists in file"""
        temp = {}
        for key, obj in FileStorage.__objects.items():
            temp[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(temp, json_file)

    def reload(self):
        """This method will deserialize the JSON
        string to a Python dictionary"""
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
