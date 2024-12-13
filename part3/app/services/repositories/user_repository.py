from app.models.user import User
from app.persistence.repository import SQLAlchemyRepository
from app.persistence import db_session


class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        return db_session.query(self.model).filter_by(email=email).first()
