#!/usr/bin/python3
from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) > 50:
            raise ValueError("Name must be a string or maximum length of 50 characters")
        self._name = value
