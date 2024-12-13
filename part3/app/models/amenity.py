from datetime import datetime
from .base import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.hybrid import hybrid_property


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    _name = Column('name', String(50), nullable=False)

    def __init__(self, name):
        super().__init__()
        if name is None:
            raise ValueError("Required attributes not specified!")
        self.name = name

    # --- Getters and Setters ---
    @hybrid_property
    def name(self):
        """ Returns value of property name """
        return self._name

    @name.setter
    def name(self, value):
        """Setter for prop name"""
        # ensure that the value is up to 50 characters after removing excess white-space
        is_valid_name = 0 < len(value.strip()) <= 50
        if is_valid_name:
            self._name = value.strip()
        else:
            raise ValueError("Invalid name length!")

    # --- Methods ---

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
