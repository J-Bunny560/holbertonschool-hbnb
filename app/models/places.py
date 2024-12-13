#!/usr/bin/python3
from app.models.base import BaseModel
from app.models.user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # User id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        try:
            if len(value) <= 100:
                self._title = value
            else:
                raise ValueError("Title maximum length of 100 characters")
        except TypeError:
            raise TypeError("Title must be a string")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is None or isinstance(value, str):
            self._description = value
        else:
            raise ValueError("Description must be a string or None")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (float, int)) and value > 0:
            self._price = value
        else:
            raise ValueError("Price must be a positive value")

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if isinstance(value, (float, int)) and -90.0 <= value <= 90.0:
            self._latitude = value
        else:
            raise ValueError(
                "Latitude must be within the range of -90.0 to 90.0")

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if isinstance(value, (float, int)) and -180.0 <= value <= 180.0:
            self._longitude = value
        else:
            raise ValueError(
                "Longitude must be within the range of -180.0 to 180.0")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        try:
            if isinstance(value, User):
                self._owner = value
            else:
                raise ValueError
        except ValueError:
            raise ValueError(
                f"User must be a valid instance of User. {str(value)}")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def toJSON(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": {
                "id": self.owner.id,
                "first_name": self.owner.first_name,
                "last_name": self.owner.last_name,
                "email": self.owner.email,
            },
            "amenities": self.amenities,
            "reviews": self.reviews,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }