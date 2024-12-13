#!/usr/bin/python3
from app.models.base import BaseModel
from app.models.places import Place
from app.models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        # Use property setters instead of direct assignment
        self.text = text          # This will use the text.setter
        self.rating = rating      # This will use the rating.setter
        self.place = place        # This will use the place.setter
        self.user = user          # This will use the user.setter

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if value is None:
            raise ValueError("Text is required and must be a string")
        if not isinstance(value, str):
            raise ValueError("Text must be a string")
        if not value.strip():  # Check if string is empty or just whitespace
            raise ValueError("Text cannot be empty")
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if 1 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("Rating must be between 1 and 5")

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise ValueError(f"Place must be a valid Place instance, got {type(value).__name__} instead")
        self._place = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise ValueError(f"User must be a valid User instance, got {type(value).__name__} instead")
        self._user = value
        
    # Add a method to convert the review to a JSON representation    
    def toJSON(self):
        """Convert review to JSON representation"""
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user.id,
            'place_id': self.place.id,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }