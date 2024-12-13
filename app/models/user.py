#!/usr/bin/python3
from app.models.base import BaseModel
import re

class User(BaseModel):
    # Class variable to store existing emails
    existing_emails = set()


    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name  # maximum length of 50 characters.
        self.last_name = last_name  # maximum length of 50 characters.
        # Required, must be unique, and should follow standard @email format validation.
        self.email = email
        self.is_admin = is_admin  # Defaults to False
        self.reviews = []
        self.places = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 0 < len(value) <= 50:
            self._first_name = value
        else:
            raise ValueError(
                "First name must be a string with a maximum length of 50 characters"
                )

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 0 < len(value) <= 50:
                self._last_name = value
        else:
            raise ValueError(
                "Last name must be a string with a maximum length of 50 characters"
                )

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if isinstance(value, str) and re.match(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
                if value in User.existing_emails:
                    raise ValueError("Email already registered")
                self._email = value
                User.existing_emails.add(value)
        else:
            raise ValueError(
                "Email must follow standard format")

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if isinstance(value, bool):
            self._is_admin = value
        else:
            raise ValueError("is_admin must be a boolean value")

    def add_review(self, review):
        """Add a review to the user."""
        self.reviews.append(review)

    def add_place(self, place):
        """Add a place to the user."""
        self.places.append(place)
    
    def toJSON(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "places": [place.toJSON() for place in self.places] if self.places else [],
            "reviews": [review.toJSON() for reviews in self.reviews] if self.reviews else [],
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }