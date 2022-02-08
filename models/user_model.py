#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel
import hashlib


class User(BaseModel):
    """Representation of a user """

    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
        self.password = self.__create_password(self.password)

    def __create_password(self, password):
        """Function that hashed the password to a MD5 value
           Args:
                password: password to be hashed
        """
        return hashlib.md5(password.encode()).hexdigest()
