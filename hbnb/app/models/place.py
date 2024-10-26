#!/usr/bin/python3
"""Place class"""

from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner