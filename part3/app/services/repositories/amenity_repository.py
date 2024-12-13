from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository
from app.persistence import db_session
from app.models.place import place_amenity, Place


class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)

    def get_amenities_by_place(self, place_id):
        return db_session.query(self.model).\
            join(place_amenity).filter_by(place_id=place_id).all()

    def create_place_amenity_link(self, place_id, amenity_id):
        new_link = place_amenity.insert().values(
            place_id=place_id, amenity_id=amenity_id)

        db_session.execute(new_link)
        db_session.commit()
        print(db_session.query(place_amenity).filter_by(
            place_id=place_id, amenity_id=amenity_id).all())
        print(f'place_id: {place_id}, amenity_id: {amenity_id}')
