#!/usr/bin/python3
"""
Contains class BaseModel
"""
import models
import uuid


class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    def __init__(self, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        for key, value in kwargs.items():
                setattr(self, key, value)

    # def __str__(self):
    #     """String representation of the BaseModel class"""
    #     return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
    #                                      self.__dict__)

    # def save(self):
    #     """updates the attribute 'updated_at' with the current datetime"""
    #     self.updated_at = datetime.utcnow()
    #     models.storage.new(self)
    #     models.storage.save()

    # def to_dict(self):
    #     """returns a dictionary containing all keys/values of the instance"""
    #     new_dict = self.__dict__.copy()
    #     if "created_at" in new_dict:
    #         new_dict["created_at"] = new_dict["created_at"].strftime(time)
    #     if "updated_at" in new_dict:
    #         new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
    #     new_dict["__class__"] = self.__class__.__name__
    #     if "_sa_instance_state" in new_dict:
    #         del new_dict["_sa_instance_state"]

    #     if "password" in new_dict:
    #         if getenv("HBNB_TYPE_STORAGE") == "db":
    #             del new_dict["password"]
    #     return new_dict

    # def delete(self):
    #     """delete the current instance from the storage"""
    #     models.storage.delete(self)
