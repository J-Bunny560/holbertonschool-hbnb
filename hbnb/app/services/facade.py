from models import user  # Use absolute imports
from models.amenity import Amenity
from persistence.repository import InMemoryRepository
from logging import getLogger


logger = getLogger(__name__)

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        if not user_data:
            raise ValueError("User data is required")
        new_user = user(**user_data)  # Ensure user is a class
        self.user_repo.add(new_user)
        return new_user

    def create_amenity(self, amenity_data):
        if not amenity_data:
            raise ValueError("Amenity data is required")
        try:
            new_amenity = Amenity(**amenity_data)
            self.amenity_repo.add(new_amenity)
            return new_amenity.__dict__
        except TypeError as e:  # Catching specific exception
            logger.error(f"Error creating amenity: {str(e)}")
            raise ValueError("Failed to create amenity due to invalid data") from e

    def get_user(self, user_id):
        if not user_id:
            raise ValueError("User ID is required")
        user = self.user_repo.get(user_id)
        if user is None:
            raise ValueError("User not found")
        return user

    def get_amenity(self, amenity_id):
        if not amenity_id:
            raise ValueError("Amenity ID is required")
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError("Amenity not found")
        return amenity

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        if not amenity_id:
            raise ValueError("Amenity ID is required")
        if not amenity_data:
            raise ValueError("Amenity data is required")
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            if hasattr(amenity, 'update'):
                try:
                    amenity.update(amenity_data)
                    return amenity
                except Exception as e:
                    logger.error(f"Error updating amenity: {str(e)}")
                    raise ValueError("Failed to update amenity") from e
            else:
                raise ValueError("Amenity object does not support updates")
        else:
            raise ValueError("Amenity not found")
