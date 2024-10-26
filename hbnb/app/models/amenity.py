#!/usr/bin/python3
"""amenity class"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """amenity class"""
    name = ""

    def __init__(self, name):
        """init"""
        super().__init__()
        self.name = name
