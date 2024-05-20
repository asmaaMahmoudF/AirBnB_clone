import json

class FileStorage:
    """The storage engine in AirBnB project"""
    
    __file_path = "file.json"
    __ojbects

    def all(self):
        """Return the dictionary ojbects"""

        return __ojbects

    def new(self, obj):
        """sets in the __objects dictionary"""

        setattr(__ojbects, type(obj).__name__.id, obj)

    def save(self):
        """This method will serialize the __objects to json string"""

        json.dump(__ojbects,__file_path)

    def reload(self):
        """This method will deserialize the Json string to py dict"""

        if __file_path:
            __objects = json.load(__file_path)

