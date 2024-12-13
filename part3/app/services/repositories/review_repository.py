from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository
from app.persistence import db_session


class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)

    def get_reviews_by_place(self, place_id):
        return db_session.query(self.model).filter_by(place_id=place_id).all()

    def get_reviews_by_user(self, user_id):
        return db_session.query(self.model).filter_by(user_id=user_id).all()
