#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format)
                else:
                    storage.new(self)

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
            format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
