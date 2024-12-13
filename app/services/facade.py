from app.persistence.repository import InMemoryRepository
from app.models.places import Place
from app.models.user import User
from app.models.amenities import Amenity
from app.models.reviews import Review 


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HBnBFacade, cls).__new__(cls)
        return cls.instance

# USER

    def create_user(self, user_data):
        """Creates a new user and saves it to the repository"""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Fetch an User by their ID"""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Fetch a user by their email address"""
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """Fetch all users"""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        try:
            self.user_repo.update(user_id, user_data)
        except (KeyError, ValueError):
            return None
        user = self.user_repo.get(user_id)
        return user

    def delete_user(self, user_id):
        """Deletes an user by ID"""
        user = self.user_repo.get(user_id)
        if user is None:
            raise ValueError("User Not Found")
        self.user_repo.delete(user_id)

# Places Facade
    def create_place(self, place_data):
        try:
            place = Place(
                title=place_data['title'],
                description=place_data['description'],
                price=place_data['price'],
                latitude=place_data['latitude'],
                longitude=place_data['longitude'],
                owner=self.get_user(place_data['owner_id']))
            self.place_repo.add(place)
            return place
        except KeyError:
            return None

    def get_place(self, place_id):
        place: Place = self.place_repo.get(place_id)
        if place:
            return place

    def get_all_places(self):
        places = []
        for place in self.place_repo.get_all():
            places.append(place.toJSON())
        return places

    def update_place(self, place_id, place_data):
        try:
            self.place_repo.update(place_id, place_data)
        except (KeyError, ValueError):
            return None
        place = self.place_repo.get(place_id)
        return place

# AMENITY

    def create_amenity(self, amenity_data):
        name = amenity_data.get('name')
        if not name:
            raise ValueError("Amenity name is required")

        existing_amenity = self.amenity_repo.get_by_attribute('name', name)
        if existing_amenity:
            raise ValueError("Amenity name already exists")

        new_amenity = Amenity(name)
        self.amenity_repo.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            return None
        return amenity

    def get_amenity_by_name(self, name):
        for amenity in self.amenity_repo.get_all():
            if amenity.name == name:
                return amenity
        return None

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            raise ValueError("ID is not found")

        if 'name' in amenity_data:
            name = amenity_data['name']
            amenity.name = name
        print("Amenity updated successfully")
        return amenity

# REVIEW

    def create_review(self, review_data):
        """Creates a new review"""
        try:
            place = self.get_place(review_data['place_id'])
            user = self.get_user(review_data['user_id'])
            if not place or not user:
                raise ValueError("Place or User not found")
                
            review = Review(
                text=review_data['text'],
                rating=review_data['rating'],
                place=place,
                user=user
            )
            self.review_repo.add(review)
            return review
        except KeyError:
            raise ValueError("Missing required review data")

    def get_review(self, review_id):
        """Fetch a review by ID"""
        return self.review_repo.get(review_id)

    def get_reviews_by_place(self, place_id):
        """Fetch all reviews for a specific place"""
        place = self.get_place(place_id)
        if not place:
            return None
        return [review for review in self.review_repo.get_all() 
                if review.place.id == place_id]

    def get_all_reviews(self):
        """Fetch all reviews"""
        return self.review_repo.get_all()

    def update_review(self, review_id, review_data):
        """Update an existing review"""
        review = self.get_review(review_id)
        if not review:
            return None
        
        if 'text' in review_data:
            review.text = review_data['text']
        if 'rating' in review_data:
            review.rating = review_data['rating']
        
        self.review_repo.update(review_id, review_data)
        return review

    def delete_review(self, review_id):
        """Delete a review"""
        review = self.get_review(review_id)
        if not review:
            return False
        self.review_repo.delete(review_id)
        return True