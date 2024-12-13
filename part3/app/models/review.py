from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from .base import BaseModel


class Review(BaseModel):
    __tablename__ = 'reviews'

    _text = Column('text', String(50), nullable=False)
    _rating = Column('rating', Integer, nullable=False)
    _user_id = Column('user_id', String(60),
                      ForeignKey('users.id'), nullable=False)
    _place_id = Column('place_id', String(60),
                       ForeignKey('places.id'), nullable=False)
    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')

    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        if text is None or rating is None or place_id is None or user_id is None:
            raise ValueError("Required attributes not specified!")

        self.text = text
        self.rating = rating
        self.place_id = place_id  # relationship - id of Place that the Review is for
        self.user_id = user_id  # relationship - id of User who wrote the Review

    # --- Getters and Setters ---
    @hybrid_property
    def text(self):
        """ Returns value of property text """
        return self._text

    @text.setter
    def text(self, value):
        """Setter for prop text"""
        # Can't think of any special checks to perform here tbh
        self._text = value

    @hybrid_property
    def rating(self):
        """ Returns value of property rating """
        return self._rating

    @rating.setter
    def rating(self, value):
        """Setter for prop rating"""
        if isinstance(value, int) and 1 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("Invalid value specified for rating")

    @hybrid_property
    def user_id(self):
        """ Returns value of property user_id """
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for prop user_id"""
        # calls the method in the facade object
        from app.services import facade

        user_exists = facade.get_user(value)
        if user_exists:
            self._user_id = value
        else:
            raise ValueError("Owner does not exist!")

    @hybrid_property
    def place_id(self):
        """ Returns value of property place_id """
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        """Setter for prop place_id"""
        # calls the method in the facade object
        from app.services import facade

        place_exists = facade.get_place(value)
        if place_exists:
            self._place_id = value
        else:
            raise ValueError("Place does not exist!")

    # --- Methods ---
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    @staticmethod
    def review_exists(review_id):
        """ Search through all Reviews to ensure the specified review_id exists """
        # Unused - the facade method get_review will handle this
